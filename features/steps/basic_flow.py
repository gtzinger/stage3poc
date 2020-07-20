import json
import requests
import ffmpy
import os

idgen_config = {
 "IDGEN_SERVER" : "10.15.129.21",
 "IDGEN_PORT" : "8081",
 "UNIQUE_ID" : "poc"
}

recording_config = {
  "CAPTURE_DURATION": "10",
  "CDN_PREFIX_URL": "http://10.15.129.21/vsg/",
  "HLS_SUFFIX_URL": "/hls-mp4/linearwm/channel1/default.m3u8",
  "RECORDINGS_FOLDER": "captures"
}

@given(u'I receive a token from IdGen')
def step_impl(context):
    get_token_url = "http://" + idgen_config["IDGEN_SERVER"] + ":" + idgen_config["IDGEN_PORT"] + \
                    "/he_ap/idgen/wm_id?unique_id=" + idgen_config["UNIQUE_ID"]
    res = requests.get(get_token_url)
    context.token = res.content.decode("utf-8")


@given(u'record video_a with the token')
def step_impl(context):
    output_file = recording_config["RECORDINGS_FOLDER"] + "/poc1.mp4"
    input_video = recording_config["CDN_PREFIX_URL"] + context.token + recording_config["HLS_SUFFIX_URL"]
    ff = ffmpy.FFmpeg(
           inputs = {input_video: None},
            outputs = {output_file: ['-t', recording_config["CAPTURE_DURATION"]] })
#    ff.cmd
    context.video = output_file
    ff.run()
    assert os.path.isfile(output_file)



@when(u'running detection on video_a')
def step_impl(context):
    raise NotImplementedError(u'STEP: When running detection on video_a')


@then(u'watermark id is detected')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then watermark id is detected')

