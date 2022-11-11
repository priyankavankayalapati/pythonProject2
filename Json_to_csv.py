import json

if __name__ == '_main_':
    try:
        with open print([
    {
        "Name": "Priya",
        "age" : 23,
        "birth year": "1999"
    }],
        print([

    {
        "Name": "Raji",
        "age" : 22,
        "birth year":2000
    },
    ]),'r') as f:
            data = json.loads(f.read())

            output = ','.join([*data[0]])
            for obj in data:
                output += f'\n{obj["Name"]},{obj["age"]},{obj["birth year"]}'

            with open('output.csv', 'w') as f:
                f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
        print([
            {
                "Name": "Priya",
                "age": 23,
                "birth year": "1999"
            },

            {
                "Name": "Raji",
                "age": 22,
                "birth year": 2000
            },
        ])

