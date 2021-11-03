from models import *
from helper import *
from random import *
from pprint import pprint
import pandas as pd
import scipy.sparse as sp
import uuid, sys, os, time, argparse
import pickle, pdb, operator, random, sys
import tensorflow as tf
from collections import defaultdict as ddict
from sklearn.metrics import precision_recall_fscore_support
from scipy.integrate import quad
import math
# survival analysis
from lifelines import KaplanMeierFitter

def integrant(x, sigma, present, end):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(((x - end) ** 2) / (2 * sigma ** 2)))


YEARMIN = -50
YEARMAX = 3000

def transform(initial_prob):
    if initial_prob < 0.4:
        return 0.0
    return 0.15 * initial_prob + 0.89


def survival_find():
    triple_time_0 = np.array([[0, 0]])
    triple_time_1 = np.array([[0, 0]])
    triple_time_2 = np.array([[0, 0]])
    triple_time_3 = np.array([[0, 0]])
    triple_time_4 = np.array([[0, 0]])
    triple_time_5 = np.array([[0, 0]])
    triple_time_6 = np.array([[0, 0]])
    triple_time_7 = np.array([[0, 0]])
    triple_time_8 = np.array([[0, 0]])
    triple_time_9 = np.array([[0, 0]])
    save_func = {}
    filename = "data/yago/large/train.txt"
    with open(filename, 'r') as filein:
        for line in filein:
            relation = line.split()[1].strip()
            start = line.split()[3].split('-')[0]
            end = line.split()[4].split('-')[0]
            if start == '####':
                start = YEARMIN
            elif start.find('#') != -1 or len(start) != 4:
                continue

            if end == '####':
                end = YEARMAX
            elif end.find('#') != -1 or len(end) != 4:
                continue

            start = int(start)
            end = int(end)

            if start > end:
                end = YEARMAX

            if end >= start:
                start = int(start)
                end = int(end)
                # 1
                if relation == "0":
                    triple_time_0 = np.append(triple_time_0, np.array([[0, 0]]), axis=0)
                    triple_time_0 = np.append(triple_time_0, np.array([[end - start, 1]]), axis=0)

                if relation == "1":
                    triple_time_1 = np.append(triple_time_1, np.array([[0, 0]]), axis=0)
                    triple_time_1 = np.append(triple_time_1, np.array([[end - start, 1]]), axis=0)

                if relation == "2":
                    triple_time_2 = np.append(triple_time_2, np.array([[0, 0]]), axis=0)
                    triple_time_2 = np.append(triple_time_2, np.array([[end - start, 1]]), axis=0)

                if relation == "3":
                    triple_time_3 = np.append(triple_time_3, np.array([[0, 0]]), axis=0)
                    triple_time_3 = np.append(triple_time_3, np.array([[end - start, 1]]), axis=0)

                if relation == "4":
                    triple_time_4 = np.append(triple_time_4, np.array([[0, 0]]), axis=0)
                    triple_time_4 = np.append(triple_time_4, np.array([[end - start, 1]]), axis=0)

                if relation == "5":
                    triple_time_5 = np.append(triple_time_5, np.array([[0, 0]]), axis=0)
                    triple_time_5 = np.append(triple_time_5, np.array([[end - start, 1]]), axis=0)

                if relation == "6":
                    triple_time_6 = np.append(triple_time_6, np.array([[0, 0]]), axis=0)
                    triple_time_6 = np.append(triple_time_6, np.array([[end - start, 1]]), axis=0)

                if relation == "7":
                    triple_time_7 = np.append(triple_time_7, np.array([[0, 0]]), axis=0)
                    triple_time_7 = np.append(triple_time_7, np.array([[end - start, 1]]), axis=0)

                if relation == "8":
                    triple_time_8 = np.append(triple_time_8, np.array([[0, 0]]), axis=0)
                    triple_time_8 = np.append(triple_time_8, np.array([[end - start, 1]]), axis=0)

                if relation == "9":
                    triple_time_9 = np.append(triple_time_9, np.array([[0, 0]]), axis=0)
                    triple_time_9 = np.append(triple_time_9, np.array([[end - start, 1]]), axis=0)

        # 0
        df0 = pd.DataFrame({'T': triple_time_0[:, 0], 'E': triple_time_0[:, 1]})
        T0 = df0['T']
        E0 = df0['E']
        kmf0 = KaplanMeierFitter()
        kmf0.fit(T0, E0)

        # 1
        df1 = pd.DataFrame({'T': triple_time_1[:, 0], 'E': triple_time_1[:, 1]})
        T1 = df1['T']
        E1 = df1['E']
        kmf1 = KaplanMeierFitter()
        kmf1.fit(T1, E1)

        # 2
        df2 = pd.DataFrame({'T': triple_time_2[:, 0], 'E': triple_time_2[:, 1]})
        T2 = df2['T']
        E2 = df2['E']
        kmf2 = KaplanMeierFitter()
        kmf2.fit(T2, E2)

        # 3
        df3 = pd.DataFrame({'T': triple_time_3[:, 0], 'E': triple_time_3[:, 1]})
        T3 = df3['T']
        E3 = df3['E']
        kmf3 = KaplanMeierFitter()
        kmf3.fit(T3, E3)

        # 4
        df4 = pd.DataFrame({'T': triple_time_4[:, 0], 'E': triple_time_4[:, 1]})
        T4 = df4['T']
        E4 = df4['E']
        kmf4 = KaplanMeierFitter()
        kmf4.fit(T4, E4)

        # 5
        df5 = pd.DataFrame({'T': triple_time_5[:, 0], 'E': triple_time_5[:, 1]})
        T5 = df5['T']
        E5 = df5['E']
        kmf5 = KaplanMeierFitter()
        kmf5.fit(T5, E5)

        # 6
        df6 = pd.DataFrame({'T': triple_time_6[:, 0], 'E': triple_time_6[:, 1]})
        T6 = df6['T']
        E6 = df6['E']
        kmf6 = KaplanMeierFitter()
        kmf6.fit(T6, E6)
        # 7
        df7 = pd.DataFrame({'T': triple_time_7[:, 0], 'E': triple_time_7[:, 1]})
        T7 = df7['T']
        E7 = df7['E']
        kmf7 = KaplanMeierFitter()
        kmf7.fit(T7, E7)

        # 8
        df8 = pd.DataFrame({'T': triple_time_8[:, 0], 'E': triple_time_8[:, 1]})
        T8 = df8['T']
        E8 = df8['E']
        kmf8 = KaplanMeierFitter()
        kmf8.fit(T8, E8)

        # 9
        df9 = pd.DataFrame({'T': triple_time_9[:, 0], 'E': triple_time_9[:, 1]})
        T9 = df9['T']
        E9 = df9['E']
        kmf9 = KaplanMeierFitter()
        kmf9.fit(T9, E9)

        save_func["0"] = kmf0
        save_func["1"] = kmf1
        save_func["2"] = kmf2
        save_func["3"] = kmf3
        save_func["4"] = kmf4
        save_func["5"] = kmf5
        save_func["6"] = kmf6
        save_func["7"] = kmf7
        save_func["8"] = kmf8
        save_func["9"] = kmf9

        return save_func


class HyTE(Model):
    def read_valid(self, filename):
        valid_triples = []
        with open(filename, 'r') as filein:
            temp = []
            for line in filein:
                temp = [int(x.strip()) for x in line.split()[0:3]]
                temp.append([line.split()[3], line.split()[4]])
                valid_triples.append(temp)
        return valid_triples

    def getOneHot(self, start_data, end_data, num_class):
        temp = np.zeros((len(start_data), num_class), np.float32)
        for i, ele in enumerate(start_data):
            if end_data[i] >= start_data[i]:
                temp[i, start_data[i]:end_data[i] + 1] = 1 / (end_data[i] + 1 - start_data[i])
            else:
                pdb.set_trace()
        return temp

    def getBatches(self, data, shuffle=True):
        if shuffle: random.shuffle(data)
        num_batches = len(data) // self.p.batch_size

        for i in range(num_batches):
            start_idx = i * self.p.batch_size
            yield data[start_idx: start_idx + self.p.batch_size]

    def create_year2id(self, triple_time):
        year2id = dict()
        freq = ddict(int)
        count = 0
        year_list = []

        for k, v in triple_time.items():
            try:
                start = v[0].split('-')[0]
                end = v[1].split('-')[0]
            except:
                pdb.set_trace()

            if start.find('#') == -1 and len(start) == 4: year_list.append(int(start))
            if end.find('#') == -1 and len(end) == 4: year_list.append(int(end))

        # for k,v in entity_time.items():
        # 	start = v[0].split('-')[0]
        # 	end = v[1].split('-')[0]

        # 	if start.find('#') == -1 and len(start) == 4: year_list.append(int(start))
        # 	if end.find('#') == -1 and len(end) ==4: year_list.append(int(end))
        # 	# if int(start) > int(end):
        # 	# 	pdb.set_trace()

        year_list.sort()
        for year in year_list:
            freq[year] = freq[year] + 1

        year_class = []
        count = 0
        for key in sorted(freq.keys()):
            count += freq[key]
            if count > 300:
                year_class.append(key)
                count = 0
        prev_year = 0
        i = 0
        for i, yr in enumerate(year_class):
            year2id[(prev_year, yr)] = i
            prev_year = yr + 1
        year2id[(prev_year, max(year_list))] = i + 1
        self.year_list = year_list

        # for k,v in entity_time.items():
        # 	if v[0] == '####-##-##' or v[1] == '####-##-##':
        # 		continue
        # 	if len(v[0].split('-')[0])!=4 or len(v[1].split('-')[0])!=4:
        # 		continue
        # 	start = v[0].split('-')[0]
        # 	end = v[1].split('-')[0]
        # for start in start_list:
        # 	if start not in start_year2id:
        # 		start_year2id[start] = count_start
        # 		count_start+=1

        # for end in end_list:
        # 	if end not in end_year2id:
        # 		end_year2id[end] = count_end
        # 		count_end+=1

        return year2id

    def get_span_ids(self, start, end):
        start = int(start)
        end = int(end)
        if start > end:
            end = YEARMAX

        if start == YEARMIN:
            start_lbl = 0
        else:
            for key, lbl in sorted(self.year2id.items(), key=lambda x: x[1]):
                if start >= key[0] and start <= key[1]:
                    start_lbl = lbl

        if end == YEARMAX:
            end_lbl = len(self.year2id.keys()) - 1
        else:
            for key, lbl in sorted(self.year2id.items(), key=lambda x: x[1]):
                if end >= key[0] and end <= key[1]:
                    end_lbl = lbl
        return start_lbl, end_lbl

    def create_id_labels(self, triple_time, dtype):
        YEARMAX = 3000
        YEARMIN = -50

        inp_idx, start_idx, end_idx = [], [], []

        for k, v in triple_time.items():
            start = v[0].split('-')[0]
            end = v[1].split('-')[0]
            if start == '####':
                start = YEARMIN
            elif start.find('#') != -1 or len(start) != 4:
                continue

            if end == '####':
                end = YEARMAX
            elif end.find('#') != -1 or len(end) != 4:
                continue

            start = int(start)
            end = int(end)

            if start > end:
                end = YEARMAX
            inp_idx.append(k)
            if start == YEARMIN:
                start_idx.append(0)
            else:
                for key, lbl in sorted(self.year2id.items(), key=lambda x: x[1]):
                    if start >= key[0] and start <= key[1]:
                        start_idx.append(lbl)

            if end == YEARMAX:
                end_idx.append(len(self.year2id.keys()) - 1)
            else:
                for key, lbl in sorted(self.year2id.items(), key=lambda x: x[1]):
                    if end >= key[0] and end <= key[1]:
                        end_idx.append(lbl)

        return inp_idx, start_idx, end_idx

    def load_data(self):
        self.id2year = {'1': 1829, '0': 0, '2': 1857, '3': 1875, '4': 1889, '5': 1899, '6': 1906, '7': 1911, '8': 1916,
                        '9': 1920, '10': 1924, '11': 1927, '12': 1930, '13': 1933, '14': 1937, '15': 1940, '16': 1943,
                        '17': 1946, '18': 1949, '19': 1952, '20': 1955,
                        '21': 1958, '22': 1961, '23': 1964, '24': 1966, '25': 1968, '26': 1970, '27': 1972, '28': 1974,
                        '29': 1976, '30': 1978, '31': 1980, '32': 1982, '33': 1984,
                        '34': 1986, '35': 1988, '36': 1990, '37': 1992, '38': 1994, '39': 1996, '40': 1997, '41': 1998,
                        '42': 1999, '43': 2000, '44': 2001, '45': 2002,
                        '46': 2003, '47': 2004, '48': 2005, '49': 2006, '50': 2007, '51': 2008, '52': 2009, '53': 2010,
                        '54': 2011, '55': 2012, '56': 2013, '57': 2014, '58': 2015,
                        '59': 2016, '60': 2017}

        triple_set = []
        with open(self.p.triple2id, 'r') as filein:
            for line in filein:
                tup = (int(line.split()[0].strip()), int(line.split()[1].strip()), int(line.split()[2].strip()))
                triple_set.append(tup)
        triple_set = set(triple_set)

        train_triples = []
        self.start_time, self.end_time, self.num_class = ddict(dict), ddict(dict), ddict(dict)
        triple_time, entity_time = dict(), dict()
        self.inp_idx, self.start_idx, self.end_idx, self.labels = ddict(list), ddict(list), ddict(list), ddict(list)
        self.variance_idx = ddict(list)  # TODO add a list of variance
        max_ent, max_rel, count = 0, 0, 0

        with open(self.p.dataset, 'r') as filein:
            for line in filein:
                train_triples.append([int(x.strip()) for x in line.split()[0:3]])
                triple_time[count] = [x.split('-')[0] for x in line.split()[3:5]]
                count += 1

        # self.start_time['triple'], self.end_time['triple'] = self.create_year2id(triple_time,'triple')

        with open(self.p.entity2id, 'r', encoding="utf-8") as filein2:
            for line in filein2:
                # entity_time[int(line.split('\t')[1])]=[x.split()[0] for x in line.split()[2:4]]
                max_ent = max_ent + 1

        self.year2id = self.create_year2id(triple_time)
        # self.start_time['entity'], self.end_time['entity'] = self.create_year2id(entity_time,'entiy')
        # self.inp_idx['entity'],self.start_idx['entity'], self.end_idx['entity'] = self.create_id_labels(entity_time,'entity')
        self.inp_idx['triple'], self.start_idx['triple'], self.end_idx['triple'] = self.create_id_labels(triple_time,
                                                                                                         'triple')
        # pdb.set_trace()
        for i, ele in enumerate(self.inp_idx['entity']):
            if self.start_idx['entity'][i] > self.end_idx['entity'][i]:
                print(self.inp_idx['entity'][i], self.start_idx['entity'][i], self.end_idx['entity'][i])
        self.num_class = len(self.year2id.keys())

        keep_idx = set(self.inp_idx['triple'])
        for i in range(len(train_triples) - 1, -1, -1):
            if i not in keep_idx:
                del train_triples[i]
                del triple_time[i]
            # times.remove(element)  # TODO delete time as well

        times = list(triple_time.values())

        with open(self.p.relation2id, 'r') as filein3:
            for line in filein3:
                max_rel = max_rel + 1
        index = randint(1, len(train_triples)) - 1

        posh, rela, post = zip(*train_triples)
        head, rel, tail = zip(*train_triples)

        posh = list(posh)
        post = list(post)
        rela = list(rela)

        head = list(head)
        tail = list(tail)
        rel = list(rel)

        # print(len(head))
        print(len(posh))
        print(len(times))
        for k in range(len(posh)):
            self.variance_idx['triple'].append(1.00)

        for i in range(len(posh)):
            if self.start_idx['triple'][i] < self.end_idx['triple'][i]:
                for j in range(self.start_idx['triple'][i] + 1, self.end_idx['triple'][i] + 1):
                    head.append(posh[i])
                    rel.append(rela[i])
                    tail.append(post[i])
                    self.start_idx['triple'].append(j)
                    start_temp = times[i][0]
                    end_temp = times[i][1]
                    if start_temp == '####':
                        start_temp = YEARMIN
                    if end_temp == '####':
                        end_temp = YEARMAX
                    present_temp = self.id2year[str(j)]
                    # sigma_temp = self.variance[str(rela[i])]
                    # print("start: {0}, present: {1}, end: {2}, sig: {3}".format(start_temp, present_temp, end_temp, sigma_temp))
                    # print("length {0}".format(len(triple_time)))
                    # print("testing {0}".format(triple_time[2][0]))
                    # c = 1 - quad(integrant, int(start_temp), int(present_temp),
                    #               (int(sigma_temp), int(present_temp), int(end_temp)))[0]
                    if int(present_temp) - int(start_temp) >= 0:
                        c = self.km_dict[str(rela[i])].survival_function_at_times(int(present_temp) - int(start_temp)).values[0]
                        c = transform(c)
                        # print(c)
                    else:
                        c = 1.0
                    # print(c)
                    self.variance_idx['triple'].append(c)

        print(len(head))

        print("start idx")
        print(len(self.start_idx['triple']))
        print("variance")
        print(len(self.variance_idx['triple']))

        self.ph, self.pt, self.r, self.nh, self.nt, self.triple_time, self.valid_list = [], [], [], [], [], [], []
        for triple in range(len(head)):
            neg_set = set()
            for k in range(self.p.M):
                possible_head = randint(0, max_ent - 1)
                while (possible_head, rel[triple], tail[triple]) in triple_set or (
                        possible_head, rel[triple], tail[triple]) in neg_set:
                    possible_head = randint(0, max_ent - 1)
                self.nh.append(possible_head)
                self.nt.append(tail[triple])
                self.r.append(rel[triple])
                # print(rel[triple])
                self.ph.append(head[triple])
                self.pt.append(tail[triple])
                self.triple_time.append(self.start_idx['triple'][triple])
                self.valid_list.append(self.variance_idx['triple'][triple])
                neg_set.add((possible_head, rel[triple], tail[triple]))

        for triple in range(len(tail)):
            neg_set = set()
            for k in range(self.p.M):
                possible_tail = randint(0, max_ent - 1)
                while (head[triple], rel[triple], possible_tail) in triple_set or (
                        head[triple], rel[triple], possible_tail) in neg_set:
                    possible_tail = randint(0, max_ent - 1)
                self.nh.append(head[triple])
                self.nt.append(possible_tail)
                self.r.append(rel[triple])
                self.ph.append(head[triple])
                self.pt.append(tail[triple])
                self.triple_time.append(self.start_idx['triple'][triple])
                self.valid_list.append(self.variance_idx['triple'][triple])
                neg_set.add((head[triple], rel[triple], possible_tail))

        # self.triple_time = triple_time
        # self.entity_time = entity_time
        self.max_rel = max_rel
        self.max_ent = max_ent
        self.max_time = len(self.year2id.keys())
        self.data = list(zip(self.ph, self.pt, self.r, self.nh, self.nt, self.triple_time, self.valid_list))
        self.data = self.data + self.data[0:self.p.batch_size]

    def calculated_score_for_positive_elements(self, t, epoch, f_valid, eval_mode='valid'):
        loss = np.zeros(self.max_ent)
        start_trip = t[3][0].split('-')[0]
        end_trip = t[3][1].split('-')[0]
        if start_trip == '####':
            start_trip = YEARMIN
        elif start_trip.find('#') != -1 or len(start_trip) != 4:
            return

        if end_trip == '####':
            end_trip = YEARMAX
        elif end_trip.find('#') != -1 or len(end_trip) != 4:
            return

        start_lbl, end_lbl = self.get_span_ids(start_trip, end_trip)

        if eval_mode == 'test':
            f_valid.write(str(t[0]) + '\t' + str(t[1]) + '\t' + str(t[2]) + '\n')
        elif eval_mode == 'valid' and epoch == self.p.test_freq:
            f_valid.write(str(t[0]) + '\t' + str(t[1]) + '\t' + str(t[2]) + '\n')

        # print("looking at program?????????????????1111111111")
        pos_head = sess.run(self.pos, feed_dict={self.pos_head: np.array([t[0]]).reshape(-1, 1),
                                                 self.rel: np.array([t[1]]).reshape(-1, 1),
                                                 self.pos_tail: np.array([t[2]]).reshape(-1, 1),
                                                 self.start_year: np.array([start_lbl] * self.max_ent),
                                                 self.end_year: np.array([end_lbl] * self.max_ent),
                                                 self.mode: -1,
                                                 self.pred_mode: 1,
                                                 self.query_mode: 1,
                                                 self.valid_placeholder: np.array([1]).reshape(-1, 1)
                                                 })
        pos_head = np.squeeze(pos_head)

        pos_tail = sess.run(self.pos, feed_dict={self.pos_head: np.array([t[0]]).reshape(-1, 1),
                                                 self.rel: np.array([t[1]]).reshape(-1, 1),
                                                 self.pos_tail: np.array([t[2]]).reshape(-1, 1),
                                                 self.start_year: np.array([start_lbl] * self.max_ent),
                                                 self.end_year: np.array([end_lbl] * self.max_ent),
                                                 self.mode: -1,
                                                 self.pred_mode: -1,
                                                 self.query_mode: 1,
                                                 self.valid_placeholder: np.array([1]).reshape(-1, 1)
                                                 })
        pos_tail = np.squeeze(pos_tail)

        pos_rel = sess.run(self.pos, feed_dict={self.pos_head: np.array([t[0]]).reshape(-1, 1),
                                                self.rel: np.array([t[1]]).reshape(-1, 1),
                                                self.pos_tail: np.array([t[2]]).reshape(-1, 1),
                                                self.start_year: np.array([start_lbl] * self.max_rel),
                                                self.end_year: np.array([end_lbl] * self.max_rel),
                                                self.mode: -1,
                                                self.pred_mode: -1,
                                                self.query_mode: -1,
                                                self.valid_placeholder: np.array([1]).reshape(-1, 1)
                                                })
        pos_rel = np.squeeze(pos_rel)

        return pos_head, pos_tail, pos_rel

    def add_placeholders(self):
        self.start_year = tf.placeholder(tf.int32, shape=[None], name='start_time')
        self.end_year = tf.placeholder(tf.int32, shape=[None], name='end_time')
        self.pos_head = tf.placeholder(tf.int32, [None, 1])
        self.pos_tail = tf.placeholder(tf.int32, [None, 1])
        self.rel = tf.placeholder(tf.int32, [None, 1])
        self.neg_head = tf.placeholder(tf.int32, [None, 1])
        self.neg_tail = tf.placeholder(tf.int32, [None, 1])
        self.mode = tf.placeholder(tf.int32, shape=())
        self.pred_mode = tf.placeholder(tf.int32, shape=())
        self.query_mode = tf.placeholder(tf.int32, shape=())
        self.valid_placeholder =  tf.placeholder(tf.float32, shape=[None, 1])


    def create_feed_dict(self, batch, wLabels=True, dtype='train'):
        ph, pt, r, nh, nt, start_idx, valid = zip(*batch)
        feed_dict = {}
        feed_dict[self.pos_head] = np.array(ph).reshape(-1, 1)
        feed_dict[self.pos_tail] = np.array(pt).reshape(-1, 1)
        feed_dict[self.rel] = np.array(r).reshape(-1, 1)
        feed_dict[self.start_year] = np.array(start_idx)
        feed_dict[self.valid_placeholder] = np.array(valid).reshape(-1, 1)
        # print("valid")
        # print(self.pos_head)


        # feed_dict[self.valid_placeholder] = np.array(valid)
        # feed_dict[self.valid_placeholder] = valid
        # feed_dict[self.end_year]   = np.array(end_idx)
        if dtype == 'train':
            feed_dict[self.neg_head] = np.array(nh).reshape(-1, 1)
            feed_dict[self.neg_tail] = np.array(nt).reshape(-1, 1)
            feed_dict[self.mode] = 1
            feed_dict[self.pred_mode] = 0
            feed_dict[self.query_mode] = 0
        else:
            feed_dict[self.mode] = -1

        return feed_dict

    def time_projection(self, data, t):
        inner_prod = tf.tile(tf.expand_dims(tf.reduce_sum(data * t, axis=1), axis=1), [1, self.p.inp_dim])
        prod = t * inner_prod
        data = data - prod
        return data

    def add_model(self):
        # nn_in = self.input_x
        with tf.name_scope("embedding"):
            self.ent_embeddings = tf.get_variable(name="ent_embedding", shape=[self.max_ent, self.p.inp_dim],
                                                  initializer=tf.contrib.layers.xavier_initializer(uniform=False),
                                                  regularizer=self.regularizer)
            self.rel_embeddings = tf.get_variable(name="rel_embedding", shape=[self.max_rel, self.p.inp_dim],
                                                  initializer=tf.contrib.layers.xavier_initializer(uniform=False),
                                                  regularizer=self.regularizer)
            self.time_embeddings = tf.get_variable(name="time_embedding", shape=[self.max_time, self.p.inp_dim],
                                                   initializer=tf.contrib.layers.xavier_initializer(uniform=False))

        transE_in_dim = self.p.inp_dim
        transE_in = self.ent_embeddings
        ####################------------------------ time aware GCN MODEL ---------------------------##############

        ## Some transE style model ####

        neutral = tf.constant(0)  ## mode = 1 for train mode = -1 test
        test_type = tf.constant(0)  ##  pred_mode = 1 for head -1 for tail
        query_type = tf.constant(0)  ## query mode  =1 for head tail , -1 for rel

        def f_train():
            pos_h_e = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.pos_head))
            pos_t_e = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.pos_tail))
            pos_r_e = tf.squeeze(tf.nn.embedding_lookup(self.rel_embeddings, self.rel))
            return pos_h_e, pos_t_e, pos_r_e

        def f_test():
            def head_tail_query():
                def f_head():
                    e2 = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.pos_tail))
                    pos_h_e = transE_in
                    pos_t_e = tf.reshape(tf.tile(e2, [self.max_ent]), (self.max_ent, transE_in_dim))
                    return pos_h_e, pos_t_e

                def f_tail():
                    e1 = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.pos_head))
                    pos_h_e = tf.reshape(tf.tile(e1, [self.max_ent]), (self.max_ent, transE_in_dim))
                    pos_t_e = transE_in
                    return pos_h_e, pos_t_e

                pos_h_e, pos_t_e = tf.cond(self.pred_mode > test_type, f_head, f_tail)
                r = tf.squeeze(tf.nn.embedding_lookup(self.rel_embeddings, self.rel))
                pos_r_e = tf.reshape(tf.tile(r, [self.max_ent]), (self.max_ent, transE_in_dim))
                return pos_h_e, pos_t_e, pos_r_e

            def rel_query():
                e1 = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.pos_head))
                e2 = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.pos_tail))
                pos_h_e = tf.reshape(tf.tile(e1, [self.max_rel]), (self.max_rel, transE_in_dim))
                pos_t_e = tf.reshape(tf.tile(e2, [self.max_rel]), (self.max_rel, transE_in_dim))
                pos_r_e = self.rel_embeddings
                return pos_h_e, pos_t_e, pos_r_e

            pos_h_e, pos_t_e, pos_r_e = tf.cond(self.query_mode > query_type, head_tail_query, rel_query)
            return pos_h_e, pos_t_e, pos_r_e

        pos_h_e, pos_t_e, pos_r_e = tf.cond(self.mode > neutral, f_train, f_test)
        neg_h_e = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.neg_head))
        neg_t_e = tf.squeeze(tf.nn.embedding_lookup(transE_in, self.neg_tail))

        #### ----- time -----###
        t_1 = tf.squeeze(tf.nn.embedding_lookup(self.time_embeddings, self.start_time))

        pos_h_e_t_1 = self.time_projection(pos_h_e, t_1)
        neg_h_e_t_1 = self.time_projection(neg_h_e, t_1)
        pos_t_e_t_1 = self.time_projection(pos_t_e, t_1)
        neg_t_e_t_1 = self.time_projection(neg_t_e, t_1)
        pos_r_e_t_1 = self.time_projection(pos_r_e, t_1)
        # pos_r_e_t_1 = pos_r_e

        if self.p.L1_flag:
            print("just debug lol")
            print(self.valid_placeholder)

            pos = tf.reduce_sum(self.valid_placeholder * abs(pos_h_e_t_1 + pos_r_e_t_1 - pos_t_e_t_1), 1,
                                keep_dims=True)
            neg = tf.reduce_sum(self.valid_placeholder * abs(neg_h_e_t_1 + pos_r_e_t_1 - neg_t_e_t_1), 1,
                                keep_dims=True)

            print("this is it")
            #print(abs(pos_h_e_t_1 + pos_r_e_t_1 - pos_t_e_t_1))
            # print(self.valid_placeholder * abs(pos_h_e_t_1 + pos_r_e_t_1 - pos_t_e_t_1))
            #tf.Print(abs(pos_h_e_t_1 + pos_r_e_t_1 - pos_t_e_t_1).eval())

            # self.predict = pos
        else:
            print("just!!!!!!!!!!!!!!!! debug lol")
            pos = tf.reduce_sum((pos_h_e_t_1 + pos_r_e_t_1 - pos_t_e_t_1) ** 2, 1, keep_dims=True)
            neg = tf.reduce_sum((neg_h_e_t_1 + pos_r_e_t_1 - neg_t_e_t_1) ** 2, 1, keep_dims=True)
        # self.predict = pos

        '''
        debug_nn([self.pred_mode,self.mode], feed_dict = self.create_feed_dict(self.data[0:self.p.batch_size],dtype='test'))
        '''
        return pos, neg

    def add_loss(self, pos, neg):
        with tf.name_scope('Loss_op'):
            loss = tf.reduce_sum(tf.maximum(pos - neg + self.p.margin, 0))
            if self.regularizer != None: loss += tf.contrib.layers.apply_regularization(self.regularizer,
                                                                                        tf.get_collection(
                                                                                            tf.GraphKeys.REGULARIZATION_LOSSES))
            print(pos)
            print("loss {0}".format(loss))
            return loss

    def add_optimizer(self, loss):
        with tf.name_scope('Optimizer'):
            optimizer = tf.train.AdamOptimizer(self.p.lr)
            train_op = optimizer.minimize(loss)
        time_normalizer = tf.assign(self.time_embeddings, tf.nn.l2_normalize(self.time_embeddings, dim=1))
        return train_op

    def __init__(self, params):
        self.reading()
        self.km_dict = survival_find()
        self.p = params
        self.p.batch_size = self.p.batch_size
        if self.p.l2 == 0.0:
            self.regularizer = None
        else:
            self.regularizer = tf.contrib.layers.l2_regularizer(scale=self.p.l2)
        self.load_data()
        self.nbatches = len(self.data) // self.p.batch_size
        self.add_placeholders()
        self.pos, neg = self.add_model()
        self.loss = self.add_loss(self.pos, neg)
        self.train_op = self.add_optimizer(self.loss)
        self.merged_summ = tf.summary.merge_all()
        self.summ_writer = None
        self.id2year = {}
        self.id2year = {'1': 1829, '0': 0, '2': 1857, '3': 1875, '4': 1889, '5': 1899, '6': 1906, '7': 1911, '8': 1916,
                        '9': 1920, '10': 1924, '11': 1927, '12': 1930, '13': 1933, '14': 1937, '15': 1940, '16': 1943,
                        '17': 1946, '18': 1949, '19': 1952, '20': 1955,
                        '21': 1958, '22': 1961, '23': 1964, '24': 1966, '25': 1968, '26': 1970, '27': 1972, '28': 1974,
                        '29': 1976, '30': 1978, '31': 1980, '32': 1982, '33': 1984,
                        '34': 1986, '35': 1988, '36': 1990, '37': 1992, '38': 1994, '39': 1996, '40': 1997, '41': 1998,
                        '42': 1999, '43': 2000, '44': 2001, '45': 2002,
                        '46': 2003, '47': 2004, '48': 2005, '49': 2006, '50': 2007, '51': 2008, '52': 2009, '53': 2010,
                        '54': 2011, '55': 2012, '56': 2013, '57': 2014, '58': 2015,
                        '59': 2016, '60': 2017}
        print('model done')

    def run_epoch(self, sess, data, epoch):
        drop_rate = self.p.dropout

        losses = []
        # total_correct, total_cnt = 0, 0

        for step, batch in enumerate(self.getBatches(data, shuffle)):
            feed = self.create_feed_dict(batch)
            l, a = sess.run([self.loss, self.train_op], feed_dict=feed)
            losses.append(l)
        return np.mean(losses)

    def fit(self, sess):
        saver = tf.train.Saver(max_to_keep=None)
        save_dir = 'checkpoints/' + self.p.name + '/'
        if not os.path.exists(save_dir): os.makedirs(save_dir)
        save_dir_results = './results/' + self.p.name + '/'
        if not os.path.exists(save_dir_results): os.makedirs(save_dir_results)
        if self.p.restore:
            save_path = os.path.join(save_dir, 'epoch_{}'.format(self.p.restore_epoch))
            saver.restore(sess, save_path)

        if not self.p.onlyTest:
            print('start fitting')
            validation_data = self.read_valid(self.p.valid_data)
            for epoch in range(self.p.max_epochs):
                l = self.run_epoch(sess, self.data, epoch)
                if epoch % 50 == 0:
                    print('Epoch {}\tLoss {}\t model {}'.format(epoch, l, self.p.name))

                if epoch % self.p.test_freq == 0 and epoch != 0:
                    save_path = os.path.join(save_dir, 'epoch_{}'.format(epoch))  ## -- check pointing -- ##
                    saver.save(sess=sess, save_path=save_path)
                    if epoch == self.p.test_freq:
                        f_valid = open(save_dir_results + '/valid.txt', 'w')

                    fileout_head = open(save_dir_results + '/valid_head_pred_{}.txt'.format(epoch), 'w')
                    fileout_tail = open(save_dir_results + '/valid_tail_pred_{}.txt'.format(epoch), 'w')
                    fileout_rel = open(save_dir_results + '/valid_rel_pred_{}.txt'.format(epoch), 'w')
                    for i, t in enumerate(validation_data):
                        score = self.calculated_score_for_positive_elements(t, epoch, f_valid, 'valid')
                        if score:
                            fileout_head.write(' '.join([str(x) for x in score[0]]) + '\n')
                            fileout_tail.write(' '.join([str(x) for x in score[1]]) + '\n')
                            fileout_rel.write(' '.join([str(x) for x in score[2]]) + '\n')

                        if i % 500 == 0:
                            print('{}. no of valid_triples complete'.format(i))

                    fileout_head.close()
                    fileout_tail.close()
                    fileout_rel.close()
                    if epoch == self.p.test_freq:
                        f_valid.close()
                    print("Validation Ended")
        else:
            print('start Testing')
            test_data = self.read_valid(self.p.test_data)
            f_test = open(save_dir_results + '/test.txt', 'w')
            fileout_head = open(save_dir_results + '/test_head_pred_{}.txt'.format(self.p.restore_epoch), 'w')
            fileout_tail = open(save_dir_results + '/test_tail_pred_{}.txt'.format(self.p.restore_epoch), 'w')
            fileout_rel = open(save_dir_results + '/test_rel_pred_{}.txt'.format(self.p.restore_epoch), 'w')
            for i, t in enumerate(test_data):
                score = self.calculated_score_for_positive_elements(t, self.p.restore_epoch, f_test, 'test')
                fileout_head.write(' '.join([str(x) for x in score[0]]) + '\n')
                fileout_tail.write(' '.join([str(x) for x in score[1]]) + '\n')
                fileout_rel.write(' '.join([str(x) for x in score[2]]) + '\n')

                if i % 500 == 0:
                    print('{}. no of test_triples complete'.format(i))
            fileout_head.close()
            fileout_tail.close()
            fileout_rel.close()
            print("Test ended")

    def reading(self):
        variance_path = 'data/' + 'yago' + '/' + 'large' + '/variance.txt'
        self.variance = json.load(open(variance_path, 'r'))
        print(self.variance)
        self.id2year = {'1': 1829, '0': 0, '2': 1857, '3': 1875, '4': 1889, '5': 1899, '6': 1906, '7': 1911, '8': 1916,
                        '9': 1920, '10': 1924, '11': 1927, '12': 1930, '13': 1933, '14': 1937, '15': 1940, '16': 1943,
                        '17': 1946, '18': 1949, '19': 1952, '20': 1955,
                        '21': 1958, '22': 1961, '23': 1964, '24': 1966, '25': 1968, '26': 1970, '27': 1972, '28': 1974,
                        '29': 1976, '30': 1978, '31': 1980, '32': 1982, '33': 1984,
                        '34': 1986, '35': 1988, '36': 1990, '37': 1992, '38': 1994, '39': 1996, '40': 1997, '41': 1998,
                        '42': 1999, '43': 2000, '44': 2001, '45': 2002,
                        '46': 2003, '47': 2004, '48': 2005, '49': 2006, '50': 2007, '51': 2008, '52': 2009, '53': 2010,
                        '54': 2011, '55': 2012, '56': 2013, '57': 2014, '58': 2015,
                        '59': 2016, '60': 2017}


if __name__ == "__main__":
    print('here in main')
    parser = argparse.ArgumentParser(description='HyTE')

    parser.add_argument('-data_type', dest="data_type", default='yago', choices=['yago', 'wiki_data'],
                        help='dataset to choose')
    parser.add_argument('-version', dest='version', default='large', choices=['large', 'small'],
                        help='data version to choose')
    parser.add_argument('-test_freq', dest="test_freq", default=25, type=int, help='Batch size')
    parser.add_argument('-neg_sample', dest="M", default=5, type=int, help='Batch size')
    parser.add_argument('-gpu', dest="gpu", default='1', help='GPU to use')
    parser.add_argument('-name', dest="name", default='test_' + str(uuid.uuid4()), help='Name of the run')
    parser.add_argument('-drop', dest="dropout", default=1.0, type=float, help='Dropout for full connected layer')
    parser.add_argument('-rdrop', dest="rec_dropout", default=1.0, type=float, help='Recurrent dropout for LSTM')
    parser.add_argument('-lr', dest="lr", default=0.0001, type=float, help='Learning rate')
    parser.add_argument('-lam_1', dest="lambda_1", default=0.5, type=float, help='transE weight')
    parser.add_argument('-lam_2', dest="lambda_2", default=0.25, type=float, help='entitty loss weight')
    parser.add_argument('-margin', dest="margin", default=1, type=float, help='margin')
    parser.add_argument('-batch', dest="batch_size", default=50000, type=int, help='Batch size')
    parser.add_argument('-epoch', dest="max_epochs", default=5000, type=int, help='Max epochs')
    parser.add_argument('-l2', dest="l2", default=0.0, type=float, help='L2 regularization')
    parser.add_argument('-seed', dest="seed", default=1234, type=int, help='Seed for randomization')
    parser.add_argument('-inp_dim', dest="inp_dim", default=128, type=int, help='Hidden state dimension of Bi-LSTM')
    parser.add_argument('-L1_flag', dest="L1_flag", action='store_false', help='Hidden state dimension of FC layer')
    parser.add_argument('-onlytransE', dest="onlytransE", action='store_true',
                        help='Evaluate model on only transE loss')
    parser.add_argument('-onlyTest', dest="onlyTest", action='store_true', help='Evaluate model for test data')
    parser.add_argument('-restore', dest="restore", action='store_true',
                        help='Restore from the previous best saved model')
    parser.add_argument('-res_epoch', dest="restore_epoch", default=200, type=int,
                        help='Restore from the previous best saved model')
    args = parser.parse_args()
    args.dataset = 'data/' + args.data_type + '/' + args.version + '/train.txt'
    args.entity2id = 'data/' + args.data_type + '/' + args.version + '/entity2id.txt'
    args.relation2id = 'data/' + args.data_type + '/' + args.version + '/relation2id.txt'
    args.valid_data = 'data/' + args.data_type + '/' + args.version + '/valid.txt'
    args.test_data = 'data/' + args.data_type + '/' + args.version + '/test.txt'
    args.triple2id = 'data/' + args.data_type + '/' + args.version + '/triple2id.txt'
    # if not args.restore: args.name = args.name + '_' + time.strftime("%d_%m_%Y") + '_' + time.strftime("%H:%M:%S")
    tf.set_random_seed(args.seed)
    random.seed(args.seed)
    np.random.seed(args.seed)
    set_gpu(args.gpu)
    model = HyTE(args)
    print('model object created')
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:
        sess.run(tf.global_variables_initializer())
        print('enter fitting')
        model.fit(sess)

