import json

if __name__ == '_main_':
    try:
        with open('input.json', 'r') as f:
            data = json.loads(f.read())

            output = ','.join([*data[0]])
            for obj in data:
                output += f'\n{obj["Name"]},{obj["age"]},{obj["birth year"]}'

            with open('output.csv', 'w') as f:
                f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')

