import unittest
from src.catalyst import CatalystCenterAdapter

MOCK_CATALYST_RESPONSE = {
    "response": [
        {
            "id": "c9300-uuid-01",
            "name": "NYC-ACCESS-01",
            "overallHealth": 95,
            "ipInterfaceHealth": 100,
            "cpuHealth": 90,
            "memoryHealth": 95
        },
        {
            "id": "c9500-uuid-02",
            "name": "NYC-CORE-01",
            "overallHealth": 32,
            "ipInterfaceHealth": 20,
            "cpuHealth": 35,
            "memoryHealth": 40
        }
    ]
}

class TestCatalystCenter(unittest.TestCase):
    def test_health_parsing(self):
        devices = CatalystCenterAdapter.parse_device_health_response(MOCK_CATALYST_RESPONSE)
        self.assertEqual(len(devices), 2)
        self.assertEqual(devices[0].hostname, "nyc-access-01")
        self.assertEqual(devices[0].overall_health, 95)

    def test_critical_threshold_filtering(self):
        devices = CatalystCenterAdapter.parse_device_health_response(MOCK_CATALYST_RESPONSE)
        crit = CatalystCenterAdapter.filter_critical_devices(devices, threshold=40)
        self.assertEqual(len(crit), 1)
        self.assertEqual(crit[0].hostname, "nyc-core-01")
        self.assertEqual(crit[0].overall_health, 32)

if __name__ == "__main__":
    unittest.main()
