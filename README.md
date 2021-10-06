Learning a bit about how python can work in a similar way to
some Java projects that I've worked on in the past.

Using testcontainers to spin up a service that integration tests can
connect to verify functionality is working as intended.

Here we have a MySQL database being brought in, which we connect to
and query for the version information - which should match what we have
specified for the container.
