"""
Measurement aNd Monitoring - prometheus probes used by reposcan subsystem
"""

from prometheus_client import Counter

FAILED_AUTH = Counter('vmaas_reposcan_failed_auth_attempts', '# of failed authentication attempts')
FAILED_WEBSOCK = Counter('vmaas_reposcan_websocket_errors', '# of websocket-cnx errors')

FAILED_CVEMAP = Counter('vmaas_reposcan_failed_cvemap_reads', '# of failures attempting to read/parse Red Hat CVE data')

FAILED_REPOMD = Counter('vmaas_reposcan_failed_repo_metadata', '# of failed repo-metadata-download attempts')
FAILED_REPO = Counter('vmaas_reposcan_failed_repository', '# of failed repo-download attempts')

FAILED_IMPORT_REPO = Counter('vmaas_reposcan_failed_repository_import', '# of failed repo-import/update attempts')
FAILED_IMPORT_CVE = Counter('vmaas_reposcan_failed_cve_import', '# of failed cve-import attempts')
FAILED_UPDATE_CVE = Counter('vmaas_reposcan_failed_cve_update', '# of failed cve-update attempts')
