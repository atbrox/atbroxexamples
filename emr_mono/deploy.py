import boto
import boto.emr
from boto.emr.step import StreamingStep
from boto.emr.bootstrap_action import BootstrapAction
import time

# set your aws keys and S3 bucket, e.g. from environment or .boto
AWSKEY=
SECRETKEY=
S3_BUCKET=
NUM_INSTANCES = 1
SLAVE_INSTANCE_TYPE = 'm1.small'
MASTER_INSTANCE_TYPE = 'm1.small'

conn = boto.connect_emr(AWSKEY,SECRETKEY)

bootstrap_step = BootstrapAction("installmono", "s3://" + S3_BUCKET + "/monobootstrap.sh",None)

step = StreamingStep(name='Wordcount',
                     mapper='s3n://' + S3_BUCKET + '/csharpmapper',
                     reducer='s3n://' + S3_BUCKET + '/fsharpreducer',
                     input='s3n://elasticmapreduce/samples/wordcount/input',
                     output='s3n://' + S3_BUCKET + '/output')

jobid = conn.run_jobflow(
    name="emr with fsharp and csharp", 
    log_uri="s3://" + S3_BUCKET + "/logs", 
    steps = [step],
    bootstrap_actions=[bootstrap_step],
    num_instances=NUM_INSTANCES,
    slave_instance_type=SLAVE_INSTANCE_TYPE,
    master_instance_type=MASTER_INSTANCE_TYPE,
    enable_debugging=True
)

print "finished spawning job (note: starting still takes time)"

state = conn.describe_jobflow(jobid).state
print "job state = ", state
print "job id = ", jobid
while state != u'COMPLETED':
    print time.localtime()
    time.sleep(30)
    state = conn.describe_jobflow(jobid).state
    print "job state = ", state
    print "job id = ", jobid

print "final output can be found in s3://" + S3_BUCKET + "/output" 
print "try: $ s3cmd sync s3://" + S3_BUCKET + "/output" + TIMESTAMP + " ."
