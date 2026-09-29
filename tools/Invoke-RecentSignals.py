"""Run installed last30days with public HN only and no inherited credentials.
No setup, login, publishing, stable AIP edits, or automatic candidate promotion.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

p = argparse.ArgumentParser()
p.add_argument('--mode', choices=['preflight', 'doctor', 'query'], default='preflight')
p.add_argument('--topic', default='context engineering')
p.add_argument('--run-root', type=Path)
p.add_argument('--skill-dir', type=Path)
a = p.parse_args()
skill = a.skill_dir or Path(os.environ['USERPROFILE']) / '.agents/skills/last30days'
engine = skill / 'scripts/last30days.py'
if not engine.is_file():
    p.error(f'Installed engine not found: {engine}')
root = a.run_root or Path(__file__).resolve().parents[1] / 'tmp/recent-signals'
root.mkdir(parents=True, exist_ok=True)
run = Path(tempfile.mkdtemp(prefix=a.mode + '-', dir=root))
# Deliberately allowlist environment. Do not copy API keys, proxy credentials,
# user Skill settings, browser selectors, or external provider endpoints.
env = {k: os.environ[k] for k in ('SystemRoot', 'WINDIR', 'COMSPEC', 'USERPROFILE') if k in os.environ}
env.update({
    'PATH': os.pathsep.join([str(Path(sys.executable).parent), str(Path(os.environ.get('SystemRoot', 'C:/Windows')) / 'System32')]),
    'TEMP': str(run), 'TMP': str(run), 'PYTHONUTF8': '1',
    'PYTHONDONTWRITEBYTECODE': '1', 'LAST30DAYS_CONFIG_DIR': '',
    'LAST30DAYS_SKIP_KEYCHAIN': '1', 'LAST30DAYS_TRUST_PROJECT_CONFIG': '0',
    'LAST30DAYS_DISCOVERY_QUEUE': 'off', 'LAST30DAYS_STRICT_EXIT': '1',
})
cmd = [sys.executable, '-B', str(engine), '--no-browser-cookies', '--search', 'hackernews']
if a.mode == 'preflight':
    cmd += ['--preflight', '--emit', 'json']
elif a.mode == 'doctor':
    cmd += ['doctor', '--json']
else:
    plan = {'intent': 'concept', 'freshness_mode': 'strict_recent', 'cluster_mode': 'topic',
            'subqueries': [{'label': 'primary', 'search_query': a.topic,
                           'ranking_query': f'What concrete practices and evidence concern {a.topic} for AI coding agents?',
                           'sources': ['hackernews'], 'weight': 1.0}]}
    plan_file = run / 'plan.json'
    plan_file.write_text(json.dumps(plan), encoding='utf-8')
    cmd += [a.topic, '--quick', '--days', '30', '--plan', str(plan_file), '--emit', 'json']
meta = {'command': cmd, 'mode': a.mode, 'topic': a.topic, 'source_boundary': ['hackernews'],
        'classification': 'external_candidate_signal_only', 'production_evidence': False}
try:
    with (run / 'stdout.json').open('w', encoding='utf-8') as out, (run / 'stderr.log').open('w', encoding='utf-8') as err:
        result = subprocess.run(cmd, env=env, cwd=run, stdout=out, stderr=err, timeout=180)
    meta['exit_code'] = result.returncode
except subprocess.TimeoutExpired:
    meta['exit_code'] = 124
    meta['status'] = 'timeout; not a successful query'
(run / 'run.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
print(json.dumps({'run_directory': str(run), **meta}, ensure_ascii=False))
sys.exit(meta['exit_code'])
