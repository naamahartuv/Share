from firebase import firebase


def add(URL, subject):

    fb = firebase.FirebaseApplication("https://share-2fffe.firebaseio.com/", None)
    data = {
                'URL': URL,
                'subject': subject
            }

    result = fb.post('/share-2fffe/Link', data)


def retrive(subject):
    fb = firebase.FirebaseApplication("https://share-2fffe.firebaseio.com/", None)
    result2 = fb.get('/share-2fffe/Link/', None)
    res = []
    for val in result2.values():
        if val['subject'] == subject:
            res.append(val['URL'])
    return printLink(res)

def printLink(list):
    output = ""
    for val in range(len(list)):
        output += (list[val])
        output += '<br>'

    return output
