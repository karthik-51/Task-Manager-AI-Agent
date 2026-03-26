DOCKER_RULES = [
    {
        "name": "backend_container_error",
        "patterns": ["error", "exception", "uncaught", "crash", "failed"],
        "severity": "high",
        "component": "backend",
    },
    {
        "name": "database_connection_issue",
        "patterns": ["mongo", "mongodb", "econnrefused", "connection refused", "timed out"],
        "severity": "high",
        "component": "database",
    },
    {
        "name": "missing_environment_variable",
        "patterns": ["missing", "undefined", "env", "environment variable"],
        "severity": "medium",
        "component": "backend",
    },
    {
        "name": "mail_auth_issue",
        "patterns": ["eauth", "missing credentials", "smtp", "nodemailer"],
        "severity": "medium",
        "component": "notification",
    },
]

JENKINS_RULES = [
    {
        "name": "jenkins_build_failed",
        "patterns": ["build failed", "script returned exit code 1", "error:", "failed"],
        "severity": "high",
        "component": "jenkins-build",
    },
    {
        "name": "docker_build_issue",
        "patterns": ["docker build", "failed to solve", "pull access denied", "no such image"],
        "severity": "high",
        "component": "docker-build",
    },
    {
        "name": "deploy_failed",
        "patterns": ["deploy", "permission denied", "no such file", "exit code 1", "denied"],
        "severity": "high",
        "component": "deployment",
    },
    {
        "name": "git_checkout_issue",
        "patterns": ["checkout", "repository not found", "authentication failed", "could not read"],
        "severity": "medium",
        "component": "git-checkout",
    },
]