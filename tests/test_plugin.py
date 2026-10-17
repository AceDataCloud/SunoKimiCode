import json
from pathlib import Path
import unittest
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parents[1]

class PluginContract(unittest.TestCase):
    def test_single_service_and_secret_binding(self):
        m = json.loads((ROOT / 'kimi.plugin.json').read_text())
        self.assertEqual(m['name'], 'suno-by-ace')
        self.assertEqual(list(m['mcpServers']), ['suno'])
        server = m['mcpServers']['suno']
        self.assertEqual(server['transport'], 'http')
        self.assertEqual(server['url'], 'https://suno.mcp.acedata.cloud/mcp')
        self.assertEqual(server['bearerTokenEnvVar'], 'ACEDATACLOUD_API_TOKEN')
        self.assertNotIn('headers', server)
        self.assertEqual(server['enabledTools'], ['suno_list_models', 'suno_list_actions', 'suno_generate_music', 'suno_generate_custom_music', 'suno_get_task'])
        self.assertTrue((ROOT / m['skills'] / 'suno-ace' / 'SKILL.md').is_file())
        self.assertFalse(any(k in m for k in ['tools','apps','inject','configFile','hooks']))

    def test_catalog_does_not_claim_official_status(self):
        c = json.loads((ROOT / 'docs/marketplace-candidate.json').read_text())
        self.assertEqual(len(c['plugins']), 1)
        self.assertNotIn('tier', c['plugins'][0])
        self.assertIn('/tree/codex/native-kimi-plugin-20261018', c['plugins'][0]['source'])

    def test_onboarding_links_and_assets(self):
        m = json.loads((ROOT / 'kimi.plugin.json').read_text())
        q = parse_qs(urlparse(m['interface']['websiteURL']).query)
        self.assertEqual(set(q), {'utm_source','utm_medium','utm_campaign','utm_content'})
        self.assertEqual(q['utm_source'], ['github'])
        self.assertEqual(q['utm_medium'], ['referral'])
        for f in ['get-api-key-en.png','create-api-key-en.png']:
            self.assertTrue((ROOT / 'assets/tutorial' / f).is_file())
        for file in ['README.md','readme/README_zh_Hans.md','commands/status.md']:
            self.assertTrue((ROOT / file).is_file())

if __name__ == '__main__':
    unittest.main()
