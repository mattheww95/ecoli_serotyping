#!/usr/bin/env python

"""
    Definitions for the ectyper project
"""

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'Data')
WORKPLACE_DIR = os.getcwd()

SEROTYPE_ALLELE_JSON = os.path.join(DATA_DIR, 'ectyper_alleles_db.json')
#ECOLI_MARKERS = os.path.join(DATA_DIR, 'ecoli_specific_markers.fasta')
REFSEQ_SUMMARY = os.path.join(DATA_DIR, 'assembly_summary_refseq.txt')
OSEROTYPE_GROUPS_DICT = {'1': ['O20','O137'],
                         '2': ['O28','O42'],
                         '3': ['O118','O151'],
                         '4': ['O90', 'O127'],
                         '5': ['O123', 'O186'],
                         '6': ['O46', 'O134'],
                         '7': ['O2','O50'],
                         '8': ['O107','O117'],
                         '9': ['O17','O44','O73', 'O77', 'O106'],
                         '10':['O13','O129','O135'],
                         '11':['O153','O178'],
                         '12':['O18ab', 'O18ac'],
                         '13':['O124','O164'],
                         '14':['O62','O68'],
                         '15':['O89','O101','O162'],
                         '16':['O169','O183']
                         }
MASH_URLS = ["https://rbhqaq.sn.files.1drv.com/y4mtYaMy88Tj5zKxMPXK6xEy9Tm5TxyH0rbQXJpIstNOK8L8OMTf8LhZ21P9XPT0-JbOUONzqAIsM66oaPRdMHLivwg9nyf3X4tutZ0UHGMwp4QKzD_VExiVY6KHbqtnKSIiBP3cv4Pg0kwrtyGnRys2DrvelPpz77CIQX_AZ7idSXkwcFcBuR40lF1YwdYZ9kSLYxF2kMR9CSol8Jbw2V8cg"]

HIGH_SIMILARITY_THRESHOLD_O = 0.00771 # alleles that are 99.23% apart will be reported as mixed call ~ 8 nt difference on average
MIN_O_IDENTITY_LS = 95 #low similarity group O antigen min identity threshold to pre-filter BLAST output  (identical to global threshold)
MIN_O_COVERAGE_LS = 48 #low similarity group O antigen min coverage threshold to pre-filter BLAST output (based on cross-talk study results)