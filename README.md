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

* [ML]Push to Container Registry (Make)


We are looking specifically for details to deploy the container
to a server.  These may be in the form of shell scripts or cloud
automation tooling like Ansible/Terraform/Helm/Nomad/Docker.

Discuss how to scale this application, if possible - how horizontal
scaling can be handled automatically.

* [ML] Setup a loadbalancer in front of the instances so they can be horizontally scaled as required without needing network configuration changes

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
* [ML] K/V store will not have primary key type semantics so you will have to make sure the keys are unique or you will run into collisions
* [ML] K/V store will be memory bound (I guess depends on implementation) and may have crashes while postgres will persist values between runs
* [ML] Postgres is likely slower and may have primary key problems requiring retries.
* [ML] Any sensitive data should be encrypted at rest so that attack vectors are mitigated.
* [ML] This app is particularily bad...it should be using HTTPS and POST rather than GET.  Many web servers will log the GET request (never the POST payload) so you are exposing customer sensitive information the way this is written.

    * what metrics are useful to collect
* [ML] for symplicity I used flask -> prometheus exporter but this is probably not the most robust way as it will require operation overhead of running Prometheus server (which has been known to have robustness issues)

* [ML] Queries per second (per end point, status)
* [ML] CPU (given CPU bound)
* [ML] IP labeled metrics (looking for abuse from single attacker)

    * how should metrics gathering be deployed?
* [ML] Pushed from the server to metrics collection jobs (usually this is done with an agent) (Something like OpenTelementry is usually good, GCE/GKE will natively export System metrics (CPU etc) (Used Flask -> Prometheus in the code)
* [ML] sometimes logs are used for this case, but logs are too bulky and have high latency when they need to be converted into metrics.


## Things we are looking for in your solution:

* Metrics - with a focus on diagnosing performance issues and scaling
    the system horizontally.
* [ML] Scaling horizontally would probably use latency, and CPU load to make scaling decisions

* Using Industry standard tooling is a strong benefit.  We would
    prefer to not rely on entirely custom tooling to deploy to
    production and staging enviroments.
* Manual or autoscaling the container load should have clear
    instructions.
* [ML] Didn't quite get there.  I got an GCE VM running with the contain from Google Container Registry GCR.  I would need to take this a step further and create an instance group with loadbalancer and all that great stuff.
The truth is to make this really scale you would probly just drop this into Cloud Run and you'd be done :).  But that is probably not the point of the exercise.
Using GCE or GKE would probably be my preferred option for anything that isn't completely trivial

* Logging - manage the log files in some endpoint for ingestion and
    processing.
* [ML] Setup Google Cloud Logging (or splunk etc)

## Bonus points:

* We currently use GCP as our cloud provider, solutions which can
    target GCP are definitely a bonus for us to verify your solution.
* We are investigating Nomad as a job scheduler, HCL configuration for
    Nomad including metrics would be fantastic.
* Service registration and discovery
