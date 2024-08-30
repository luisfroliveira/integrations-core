import pytest

from datadog_checks.base.constants import ServiceCheck
from datadog_checks.dev.utils import assert_service_checks


@pytest.mark.e2e
def test_check_appgate_sdp_e2e(dd_agent_check, instance):
    aggregator = dd_agent_check(instance, rate=True)
    aggregator.assert_service_check('appgate_sdp.openmetrics.health', ServiceCheck.OK, count=2)
    assert_service_checks(aggregator)