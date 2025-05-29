from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host('www', 'multitenant_project.urls', name='www'),
    host('abc', 'core.tenant_urls', name='abc'),
)