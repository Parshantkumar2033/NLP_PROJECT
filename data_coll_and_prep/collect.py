import http.client, urllib.parse
import json
import os

class collect:
    __keys = []

    def __init__(self, start, requests, save_file):
        '''
        self.start : starting file counter in which data is present
        self.end : last file counter containing  data
        '''
        self.start = start
        self.end = None
        self.requests = requests
        self.save_file = save_file
        self.open_file = None

    def data_copy(self, from_file, to_file):
        # from_file : 'marketaux_data(self.start).json'
        # to_file : appending file

        ds = None
        with open(from_file) as file1:
            ds = json.load(file1)
        with open(to_file, 'w') as file2:
            json.dump(ds, file2, indent=4)

    def merge(self, open_file, save_file):
        '''
        save_file : in which all the json data is going to merge
        open_file : starting file which contains the first json data(for today)
        '''
        from_file = open_file   
        to_file = save_file

        self.data_copy(from_file, to_file)

        def write_file(dat, save_file):
            with open(save_file, 'w') as write_file:
                json.dump(dat, write_file, indent = 4)

        # opening the file, in which we need to append the data
        d = None
        temp = None
        with open(save_file) as file1:
            d = json.load(file1)
            temp = d['data']
        print("save_file opened")

        i = self.start   # need to update for each api-key
        while (i < 1348): # self.end-1
            file_name = 'marketaux_data' + f'{i+1}' + '.json'
            with open(file_name) as file2:
                print(f"...opening {file_name}")
                dd = json.load(file2)
                if 'data' in dd:  # Check if 'data' key exists
                    y = dd['data']
                    for item in y:
                        temp.append(item)
                    print("\tfiles added")
                else:
                    print(f"Warning: 'data' key not found")
            i += 1
            if i % 100 == 0:
                print(f"Merged {i} files.")

        # writing the temp data to a single file
        write_file(d, save_file=save_file)



    def fetch_data(self):
        # self.end = self.start
        # t = None
        # conn = http.client.HTTPSConnection('api.marketaux.com')

        # for key in self.__keys:
        #     i = self.end
        #     d = None
        #     pprs = {
        #                 'api_token': key,
        #                 'symbols': 'MSFT',
        #                 'countries': 'in',
        #                 'filter_entities': 'true',
        #                 'published_before': '2022-10-14T09:44:42',
        #                 'language':'en',
        #                 'limit': 3,
        #             }
        #     params = None
        #     while(i < (self.end + self.requests)):
        #         if i == 1:
        #             pprs = {
        #                 'api_token': key,
        #                 'symbols': 'MSFT',
        #                 'countries': 'in',
        #                 'filter_entities': 'true',
        #                 'published_before': '2022-10-14T09:44:42',
        #                 'language':'en',
        #                 'limit': 3,
        #             }
        #             params = None
        #             self.open_file = 'marketaux_data' + f'{i}' + '.json'
        #         else:
        #             file_name = 'marketaux_data' + f'{i-1}' + '.json'

        #             with open(file_name, 'r') as open_file:
        #                 d = json.load(open_file)
        #                 if not d['data']:
        #                     print("Data is not present...")
        #                     flag = True
        #                     t = pprs['published_before'][:8] + str(int(pprs['published_before'][8:10])+1) + pprs['published_before'][10:19]
        #                     print(f'{t}\tDate incremented.')
        #                     break
        #                 else:
        #                     t = d['data'][-1]['published_at'][:19]
        #                 print(f"Time: {t}\tFile: {i}")
                        
        #                 pprs['published_before'] = t
        #         params = urllib.parse.urlencode(pprs)

        #         conn.request('GET', '/v1/news/all?{}'.format(params))

        #         res = conn.getresponse()
        #         data = res.read()
        #         data = data.decode('utf-8')

        #         data_dict = json.loads(data) # in the dictionary format

        #         file_name = 'marketaux_data' + f'{i}' + '.json'

        #         with open(file_name, 'w') as json_file:
        #             json.dump(data_dict, json_file, indent=4)

        #         i += 1
        #     self.end = self.end + self.requests
        self.merge('marketaux_data1.json', self.save_file)


        


if __name__ == "__main__":
    start_count = 1
    requests = int(input("Number of requests : "))
    save_file = str(input("File name to save : ")) + '.json'

    collect = collect(start_count, requests, save_file)

    collect.fetch_data()