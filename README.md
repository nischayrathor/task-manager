## task-manager

#### Building container images

***Using task tool***

* https://taskfile.dev/

```bash
task build
```

#### Running Application for local development

```bash
pip3 install -r requirements.txt
python3 main.py
```

#### Running via container image

```bash
task up
```

### How to use APP

***App health check***

```bash
curl -sS -XGET localhost:8080/health | jq .
{
  "postgres_healthy": true
}
```

***Listing all tasks***

```bash
curl -sS -XGET localhost:8080/get_tasks | jq .
[
  [
    {
      "task_id": 1,
      "task_name": "go-to-gym",
      "task_owner": "Nischay",
      "task_status": true
    }
  ],
  [
    {
      "task_id": 2,
      "task_name": "go-to-school",
      "task_owner": "Ravi",
      "task_status": true
    }
  ],
  [
    {
      "task_id": 3,
      "task_name": "go-to-temple",
      "task_owner": "Sanjay",
      "task_status": false
    }
  ]
]
```

***Get details of a single task***

```bash
curl -sS -XGET localhost:8080/get_task/1 | jq .
[
  {
    "task_id": 1,
    "task_name": "go-to-gym",
    "task_owner": "Nischay",
    "task_status": true
  }
]
```

***Adding new Task***

```bash
curl -v -XPOST localhost:8080/new_task \
    -H "Content-Type: application/json" \
    -d '{"task_id": 4, "task_name": "go-to-office", "task_owner": "Motu", "task_status": true }'
```

#### Security Scans
Using Trviy - https://github.com/aquasecurity/trivy

```bash
task security_scans
```

***Container Image***

```bash
source .env
trivy image task-manager:$TAG
```

***Code Scan***

```bash
trivy fs --scanners vuln,secret,misconfig .
```

### License

Please see the *LICENSE* for more information.

### Links
1. https://taskfile.dev/
2. https://github.com/go-task/task