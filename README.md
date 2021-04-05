# Simple bcrypt web app

This application exposes a single endpoint :

```
    http://localhost:8000/gethash/<password>/
```

and returns a JSON blob with the hex encoded salt and bcrypt hash.

gunicorn is configured with 2 workers and 2 threads.

This container has no persistent storage and is CPU bound.

----

Using this repository  - demonstrate deploying this container to a
server.

What scripts and configuration files are required to deploy this?

We are looking specifically for details to deploy the container
to a server.  These may be in the form of shell scripts or cloud
automation tooling like Ansible/Terraform/Helm/Nomad/Docker.

Discuss how to scale this application, if possible - how horizontal
scaling can be handled automatically.

This exercise should take no more than ~3 hours.

Discuss any considerations that should be made for:

* Networking:
    * Attack mitigation and detection
* Persistence:
    * Are there considerations that feature engineering should
      consider for a cloud deployment if persistence is required?
      * What considerations should feature engineering be made aware
          of in the case that we use a shared postgresql backend
          compared to a distributed k/v store when the container
          workload is being scaled?
    * what metrics are useful to collect
    * how should metrics gathering be deployed?

## Things we are looking for in your solution:

* Metrics - with a focus on diagnosing performance issues and scaling
    the system horizontally.
* Using Industry standard tooling is a strong benefit.  We would
    prefer to not rely on entirely custom tooling to deploy to
    production and staging enviroments.
* Manual or autoscaling the container load should have clear
    instructions.
* Logging - manage the log files in some endpoint for ingestion and
    processing.

## Bonus points:

* We currently use GCP as our cloud provider, solutions which can
    target GCP are definitely a bonus for us to verify your solution.
* We are investigating Nomad as a job scheduler, HCL configuration for
    Nomad including metrics would be fantastic.
* Service registration and discovery
