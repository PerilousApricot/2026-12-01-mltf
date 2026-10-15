---
layout: page
root: .
---

<div class="jumbotron">
  <div class="container">
    <h1>MLflow MLTF Gateway Tutorial</h1>
    <p class="lead">
      Learn to submit ML training jobs to high-performance computing clusters
      using the MLflow MLTF Gateway. A self-paced tutorial from installation
      to your first submitted job.
    </p>
    <p>
      <a class="btn btn-primary btn-lg" href="{{ page.root }}/episodes/01-introduction.html" role="button">Start Tutorial</a>
    </p>
  </div>
</div>

<div class="container">
  <div class="row">
    <div class="col-md-4">
      <h2>What you'll learn</h2>
      <ul>
        <li>Install and configure the MLTF Gateway client</li>
        <li>Authenticate with your institutional credentials</li>
        <li>Create MLflow Projects for your training code</li>
        <li>Configure compute resources (CPU, GPU, memory)</li>
        <li>Submit, monitor, and manage training jobs</li>
        <li>View results and artifacts in MLflow</li>
      </ul>
    </div>
    <div class="col-md-4">
      <h2>Prerequisites</h2>
      <ul>
        <li>Python 3.8+ installed</li>
        <li>Basic command line skills</li>
        <li>An institutional account (Vanderbilt or CERN)</li>
      </ul>
      <p>No prior experience with MLflow, SLURM, or OIDC required.</p>
    </div>
    <div class="col-md-4">
      <h2>Tutorial Details</h2>
      <p><strong>Estimated time:</strong> 60-90 minutes</p>
      <p><strong>Episodes:</strong> 8 self-paced lessons</p>
      <p><strong>Gateway URI:</strong></p>
      <code>https://gw.mltf.vu</code>
    </div>
  </div>

  <hr>

  <h2>Tutorial Episodes</h2>
  <ol>
    <li><a href="{{ page.root }}/episodes/01-introduction.html">Introduction to MLTF Gateway</a> (5 min)</li>
    <li><a href="{{ page.root }}/episodes/02-installation.html">Installation and Configuration</a> (10 min)</li>
    <li><a href="{{ page.root }}/episodes/03-authentication.html">Authentication</a> (10 min)</li>
    <li><a href="{{ page.root }}/episodes/04-first-project.html">Your First MLflow Project</a> (15 min)</li>
    <li><a href="{{ page.root }}/episodes/05-resource-config.html">Resource Configuration</a> (10 min)</li>
    <li><a href="{{ page.root }}/episodes/06-submit-monitor.html">Submit and Monitor Jobs</a> (10 min)</li>
    <li><a href="{{ page.root }}/episodes/07-viewing-results.html">Viewing Results</a> (10 min)</li>
    <li><a href="{{ page.root }}/episodes/08-advanced-topics.html">Advanced Topics</a> (10 min)</li>
  </ol>
</div>
