"""Cisco Catalyst Center (DNA Center) Assurance & Device Health Adapter."""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class CatalystDeviceHealth:
    """Normalized device health indicators reported by Catalyst Center Assurance."""
    device_id: str
    hostname: str
    overall_health: int
    ip_interface_health: int
    cpu_health: int
    memory_health: int


class CatalystCenterAdapter:
    """Adapter for Cisco Catalyst Center v2.3+ Intent & Assurance API payloads."""

    @staticmethod
    def parse_device_health_response(payload: Dict) -> List[CatalystDeviceHealth]:
        """
        Parses Catalyst Center API response (/dna/intent/api/v1/network-device-health).
        Extracts device identifiers and subsystem health scores.
        """
        results = []
        for item in payload.get("response", []):
            results.append(CatalystDeviceHealth(
                device_id=item.get("id", ""),
                hostname=item.get("name", "").lower(),
                overall_health=int(item.get("overallHealth", 100)),
                ip_interface_health=int(item.get("ipInterfaceHealth", 100)),
                cpu_health=int(item.get("cpuHealth", 100)),
                memory_health=int(item.get("memoryHealth", 100))
            ))
        return results

    @staticmethod
    def filter_critical_devices(devices: List[CatalystDeviceHealth], threshold: int = 40) -> List[CatalystDeviceHealth]:
        """Filters nodes falling below the minimum acceptable health score threshold."""
        return [d for d in devices if d.overall_health < threshold]
