import json
import re

dir_list = ['visdial_1.0_test', 'visdial_1.0_train', 'visdial_1.0_val']
#f_name = 'visdial_1.0_val'
for f_name in dir_list:
    with open(f_name + '/' + f_name + '.json', 'r') as f:
        data = json.load(f)

    dialogs = data['data']['dialogs']
    questions = data['data']['questions']
    result = {}
    for dialog in dialogs:
        img_id = dialog['image_id']
        cap = dialog['caption']
        question = []
        for d_data in dialog['dialog']:
            q = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'\'…》]', '', questions[d_data['question']])
            question.append(q.lower())
        result[img_id] = {'caption': cap,
                          'questions': question}

    with open('result/' + f_name + '.json', 'w') as f:
        json.dump(result, f)
