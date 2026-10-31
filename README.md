# Catalyst Center Device Health Adapter

Converts a Catalyst Center device-health response payload into typed records and filters devices below a health-score threshold.

## Main entry points

- `src.catalyst.CatalystDeviceHealth`
- `src.catalyst.CatalystCenterAdapter` (`parse_device_health_response, filter_critical_devices`)

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The project uses the Python standard library; no third-party package is required.

## Scope

This repository handles API response data only. It does not authenticate to a controller or make HTTP requests; pass it a response payload obtained from your Catalyst Center environment.
