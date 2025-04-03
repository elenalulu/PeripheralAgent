# coding: utf-8
from openai import OpenAI
import os


client = OpenAI(
    api_key = "your aliyun api", #aliyun api
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


scrip_demo = '{  scripts: [    { delay: 50, event_type: "EK", action_type: "key down", action: [67, "C", 0], type: "event" },   ],}'

scrip_demo = '''{
  scripts: [
    {
      delay: 201,
      event_type: "EM",
      action_type: "mouse move",
      action: [
        "0.48671875%",
        "0.42625%",
      ],
      type: "event",
    },
    {
      delay: 257,
      event_type: "EM",
      action_type: "mouse left down",
      action: [
        "0.32734375%",
        "0.383125%",
      ],
      type: "event",
    },
    {
      delay: 98,
      event_type: "EM",
      action_type: "mouse left up",
      action: [
        "0.32734375%",
        "0.383125%",
      ],
      type: "event",
    },
    {
      delay: 201,
      event_type: "EM",
      action_type: "mouse move",
      action: [
        "0.347265625%",
        "0.365625%",
      ],
      type: "event",
    },
    {
      delay: 816,
      event_type: "EK",
      action_type: "key down",
      action: [
        87,
        "W",
        0,
      ],
      type: "event",
    },
    {
      delay: 132,
      event_type: "EK",
      action_type: "key up",
      action: [
        87,
        "W",
        0,
      ],
      type: "event",
    },
  ],
}'''

content = scrip_demo + '\n按照上面的方式，写一个鼠标动作，在word上打出“再一次”几个字，用词语拼音的整体输入方式写。'

completion = client.chat.completions.create(
    model="deepseek-v3",  
    messages=[
        {"role": "user", "content": content}
    ],
    stream=True,
)

for chunk in completion:
    delta = chunk.choices[0].delta
    print(delta.content, end='', flush=True)
