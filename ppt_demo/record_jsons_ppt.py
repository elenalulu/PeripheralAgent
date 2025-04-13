import subprocess
import os
from openai import OpenAI
import re
import jieba

client = OpenAI(
    api_key = "your api key", #aliyun api
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def json_letter(text):
    from pypinyin import pinyin, Style

    parts = re.findall(r'([\u4e00-\u9fff]+)|([a-zA-Z]+)', text)

    result = []
    last_end = 0
    for part in parts:
        chinese, english = part

        start = text.find(chinese if chinese else english, last_end)
        if start > last_end:
            result.append(text[last_end:start]) 

        if chinese:
            result.extend(jieba.lcut(chinese))  
        elif english:
            result.append(f"~{english}~") 
        last_end = start + len(chinese if chinese else english)

    if last_end < len(text):
        result.append(text[last_end:])

    jieba_sentence = " ".join(result)
    jieba_sentence = jieba_sentence.replace('， ','，').replace('： ','：')
    print (jieba_sentence)

    pinyin_list = pinyin(jieba_sentence, style=Style.NORMAL)
    

    letters = ''
    for pinyin in pinyin_list:
        pinyin = ''.join(pinyin)
        letters += pinyin

    letter_list = []
    for letter in letters:
        letter = letter.upper()
        letter_list.append(letter)

    ascii_list = [("-", 189), ("，", 188), ("。", 190), ("~", 160), (" ", 32), ("\n", 13), ("0", 48), ("1", 49), ("2", 50), ("3", 51), ("4", 52), ("5", 53), ("6", 54), ("7", 55), ("8", 56), ("9", 57), ("A", 65), ("B", 66), ("C", 67), ("D", 68), ("E", 69), ("F", 70), ("G", 71), ("H", 72), ("I", 73), ("J", 74), ("K", 75), ("L", 76), ("M", 77), ("N", 78), ("O", 79), ("P", 80), ("Q", 81), ("R", 82), ("S", 83), ("T", 84), ("U", 85), ("V", 86), ("W", 87), ("X", 88), ("Y", 89), ("Z", 90)]

    script_output = '''{
      "scripts": [''' + '\n'

    for letter in letter_list:
      letter_ascii = 'none'
      for item in ascii_list:
          if letter == item[0]:
              letter_ascii = item[1]

      if letter == '：' or letter == ':':
        block = '''
            {
              delay: 20,
              event_type: "EK",
              action_type: "key down",
              action: [
                160,
                "Lshift",
                0,
              ],
              type: "event",
            },
            {
              delay: 20,
              event_type: "EK",
              action_type: "key down",
              action: [
                186,
                "Oem_1",
                0,
              ],
              type: "event",
            },
            {
              delay: 20,
              event_type: "EK",
              action_type: "key up",
              action: [
                186,
                "Oem_1",
                0,
              ],
              type: "event",
            },
            {
              delay: 20,
              event_type: "EK",
              action_type: "key up",
              action: [
                160,
                "Lshift",
                0,
              ],
              type: "event",
            },'''

        script_output += block

      elif letter_ascii == 13:
        block = '''
            {
              delay: 20,
              event_type: "EK",
              action_type: "key down",
              action: [
                32,
                "Space",
                0,
              ],
              type: "event",
            },
            {
              delay: 20,
              event_type: "EK",
              action_type: "key up",
              action: [
                32,
                "Space",
                0,
              ],
              type: "event",
            },
            {
              "delay": 20,
              "event_type": "EK",
              "action_type": "key down",
              "action": [13,
                "Return",
                0
              ],
              "type": "event"
            },
            {
              "delay": 20,
              "event_type": "EK",
              "action_type": "key up",
              "action": [13,
                "Return",
                0
              ],
              "type": "event"
            },\n'''

        script_output += block

      elif letter_ascii != 'none':
        block = '''{
              "delay": 20,
              "event_type": "EK",
              "action_type": "key down",
              "action": ['''+ str(letter_ascii) + ''',
                "'''+ letter + '''",
                0
              ],
              "type": "event"
            },
            {
              "delay": 20,
              "event_type": "EK",
              "action_type": "key up",
              "action": ['''+ str(letter_ascii) + ''',
                "'''+ letter + '''",
                0
              ],
              "type": "event"
            },\n'''

        script_output += block

    script_output += '\n' + '''
        {
          delay: 200,
          event_type: "EK",
          action_type: "key down",
          action: [
            32,
            "Space",
            0,
          ],
          type: "event",
        },
        {
          delay: 20,
          event_type: "EK",
          action_type: "key up",
          action: [
            32,
            "Space",
            0,
          ],
          type: "event",
        },
      ],
    }'''

    return script_output



# prompt = '写一个大模型发展史的ppt，页面之间用<page>分隔。每一页的标题前后加上<title>。要写大标题'


# # 非流式
# completion = client.chat.completions.create(
#     model="deepseek-v3",  
#     messages=[
#         {"role": "user", "content": prompt}
#     ],
# )

# output = completion.choices[0].message.content
# output = output.replace('```','').replace('json','')
# print (output)

output = '''
<title>大模型发展史</title>
<page>
<title>引言</title>
- 大模型的定义：基于深度学习的超大规模神经网络
- 大模型的重要性：推动人工智能技术发展，赋能各行各业
- 本PPT结构：从早期探索到最新突破，全面回顾大模型发展历程
</page>
<page>
<title>早期探索（2010-2015）</title>
- 背景：深度学习兴起，计算资源逐步提升
- 关键事件：
  - 2012年：AlexNet在ImageNet竞赛中夺冠，开启深度学习热潮
  - 2013年：Word2Vec提出，推动自然语言处理发展
- 局限性：模型规模较小，能力有限
</page>
<page>
<title>初步发展（2016-2018）</title>
- 背景：GPU等硬件加速技术普及，数据规模扩大
- 关键事件：
  - 2017年：Transformer架构提出，奠定大模型基础
  - 2018年：BERT模型发布，刷新多项NLP任务记录
- 特点：模型规模逐步扩大，性能显著提升
</page>
<page>
<title>快速突破（2019-2021）</title>
- 背景：计算资源进一步丰富，预训练范式成熟
- 关键事件：
  - 2020年：GPT-3发布，参数量达1750亿，展现强大生成能力
  - 2021年：多模态模型CLIP、DALL-E问世，拓展大模型应用领域
- 特点：模型规模指数级增长，能力更加通用化
</page>
<page>
<title>最新进展（2022-2023）</title>
- 背景：大模型成为AI领域核心方向，竞争激烈
- 关键事件：
  - 2022年：ChatGPT发布，引发全球关注
  - 2023年：GPT-4、PaLM 2等模型推出，能力进一步提升
- 特点：模型更加智能，应用场景更加广泛
</page>
<page>
<title>未来展望</title>
- 技术趋势：
  - 模型规模继续扩大，能力更加通用
  - 多模态、可解释性、高效训练等方向成为重点
- 应用前景：
  - 赋能教育、医疗、金融等行业
  - 推动人机交互方式变革
- 挑战与思考：
  - 伦理与安全问题
  - 资源消耗与可持续发展
</page>
<page>
<title>总结</title>
- 大模型发展历程：从早期探索到快速突破，不断刷新AI能力边界
- 大模型的意义：推动技术进步，改变社会生产生活方式
- 未来展望：持续创新，迎接挑战，共创智能未来
</page>
'''

page_list = str(output).split('<page>')

for i in range(0, len(page_list)):
    page = page_list[i]
    page = page.replace('>','').replace('<','').replace('/','').replace('page','')

    page_raw = str(page).split('title')
    title = page_raw[1]
    
    title_letter = json_letter(title)
    ppt_name = 'ppt_' + str(i+1) + '_1_1.json5' 
    ppt_name = '../keymousego/scripts/' + ppt_name
    with open(ppt_name, 'w+', encoding='utf-8') as fl:
      fl.write(title_letter)

    content = page_raw[2]
    content = content.lstrip('\n')
    content = content.rstrip('\n')

    content_letter = json_letter(content)
    ppt_name = 'ppt_' + str(i+1) + '_2_1.json5' 
    ppt_name = '../keymousego/scripts/' + ppt_name
    with open(ppt_name, 'w+', encoding='utf-8') as fl:
      fl.write(content_letter)

    create_1_0 = '''{
      scripts: [
        {
          delay: 207,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.7296875%",
            "0.4675%",
          ],
          type: "event",
        },
        {
          delay: 200,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.60390625%",
            "0.6775%",
          ],
          type: "event",
        },
        {
          delay: 200,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.476171875%",
            "0.72%",
          ],
          type: "event",
        },
        {
          delay: 184,
          event_type: "EM",
          action_type: "mouse left down",
          action: [
            "0.4359375%",
            "0.733125%",
          ],
          type: "event",
        },
        {
          delay: 113,
          event_type: "EM",
          action_type: "mouse left up",
          action: [
            "0.4359375%",
            "0.733125%",
          ],
          type: "event",
        },
        {
          delay: 231,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.4359375%",
            "0.733125%",
          ],
          type: "event",
        },
        {
          delay: 225,
          event_type: "EM",
          action_type: "mouse left down",
          action: [
            "0.430078125%",
            "0.74125%",
          ],
          type: "event",
        },
        {
          delay: 95,
          event_type: "EM",
          action_type: "mouse left up",
          action: [
            "0.430078125%",
            "0.74125%",
          ],
          type: "event",
        },
        {
          delay: 952,
          event_type: "EM",
          action_type: "mouse left down",
          action: [
            "0.430078125%",
            "0.74125%",
          ],
          type: "event",
        },
        {
          delay: 137,
          event_type: "EM",
          action_type: "mouse left up",
          action: [
            "0.430078125%",
            "0.74125%",
          ],
          type: "event",
        },
        {
          delay: 20,
          event_type: "EK",
          action_type: "key down",
          action: [
            162,
            "Lcontrol",
            1,
          ],
          type: "event",
        },
        {
          delay: 119,
          event_type: "EK",
          action_type: "key down",
          action: [
            77,
            "M",
            0,
          ],
          type: "event",
        },
        {
          delay: 20,
          event_type: "EK",
          action_type: "key up",
          action: [
            162,
            "Lcontrol",
            1,
          ],
          type: "event",
        },
        {
          delay: 128,
          event_type: "EK",
          action_type: "key up",
          action: [
            77,
            "M",
            0,
          ],
          type: "event",
        },
        {
          delay: 634,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.430078125%",
            "0.74125%",
          ],
          type: "event",
        },
        {
          delay: 201,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.385546875%",
            "0.428125%",
          ],
          type: "event",
        },
        {
          delay: 280,
          event_type: "EM",
          action_type: "mouse left down",
          action: [
            "0.389453125%",
            "0.363125%",
          ],
          type: "event",
        },
        {
          delay: 87,
          event_type: "EM",
          action_type: "mouse left up",
          action: [
            "0.389453125%",
            "0.363125%",
          ],
          type: "event",
        },
      ],
    }'''

    if i != 0:
      ppt_name = 'ppt_' + str(i+1) + '_1_0.json5' 
      ppt_name = '../keymousego/scripts/' + ppt_name
      with open(ppt_name, 'w+', encoding='utf-8') as fl:
          fl.write(create_1_0)


    create_2_0 = '''{
      scripts: [
        {
          delay: 200,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.45859375%",
            "0.53%",
          ],
          type: "event",
        },
        {
          delay: 200,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.36796875%",
            "0.611875%",
          ],
          type: "event",
        },
        {
          delay: 200,
          event_type: "EM",
          action_type: "mouse move",
          action: [
            "0.3234375%",
            "0.576875%",
          ],
          type: "event",
        },
        {
          delay: 205,
          event_type: "EM",
          action_type: "mouse left down",
          action: [
            "0.313671875%",
            "0.551875%",
          ],
          type: "event",
        },
        {
          delay: 94,
          event_type: "EM",
          action_type: "mouse left up",
          action: [
            "0.313671875%",
            "0.551875%",
          ],
          type: "event",
        },
        {
          delay: 395,
          event_type: "EM",
          action_type: "mouse left down",
          action: [
            "0.313671875%",
            "0.551875%",
          ],
          type: "event",
        },
        {
          delay: 86,
          event_type: "EM",
          action_type: "mouse left up",
          action: [
            "0.313671875%",
            "0.551875%",
          ],
          type: "event",
        },
      ],
    }'''

    ppt_name = 'ppt_' + str(i+1) + '_2_0.json5' 
    ppt_name = '../keymousego/scripts/' + ppt_name
    with open(ppt_name, 'w+', encoding='utf-8') as fl:
        fl.write(create_2_0)