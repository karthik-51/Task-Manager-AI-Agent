DOCKER_RULES = [
    {
        "name": "backend_container_error",
        "patterns": [
            "uncaught exception",
            "fatal error",
            "crash",
            "container exited",
            "exited with code",
            "node:internal",
        ],
        "severity": "high",
        "component": "backend",
    },
    {
        "name": "database_connection_issue",
        "patterns": [
            "mongo connection failed",
            "mongodb connection failed",
            "econnrefused",
            "connection refused",
            "timed out while connecting",
            "mongoserverselectionerror",
        ],
        "severity": "high",
        "component": "database",
    },
    {
        "name": "missing_environment_variable",
        "patterns": [
            "missing environment variable",
            "env is undefined",
            "jwt_secret is undefined",
            "mongo_uri is undefined",
        ],
        "severity": "medium",
        "component": "backend",
    },
    {
        "name": "mail_auth_issue",
        "patterns": [
            "eauth",
            "missing credentials for plain",
            "smtp authentication failed",
            "nodemailer",
        ],
        "severity": "medium",
        "component": "notification",
    },
]

JENKINS_RULES = [
    {
        "name": "jenkins_build_failed",
        "patterns": [
            "finished: failure",
            "build failed",
            "script returned exit code 1",
            "multiplecompilationerrorsexception",
        ],
        "severity": "high",
        "component": "jenkins-build",
    },
    {
        "name": "docker_build_issue",
        "patterns": [
            "failed to solve",
            "pull access denied",
            "no such image",
            "docker build",
        ],
        "severity": "high",
        "component": "docker-build",
    },
    {
        "name": "deploy_failed",
        "patterns": [
            "deploy failed",
            "permission denied",
            "no such file",
            "host key verification failed",
            "ssh:",
        ],
        "severity": "high",
        "component": "deployment",
    },
    {
        "name": "git_checkout_issue",
        "patterns": [
            "repository not found",
            "authentication failed",
            "could not read from remote repository",
        ],
        "severity": "medium",
        "component": "git-checkout",
    },
]