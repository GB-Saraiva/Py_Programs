from ast import Try
import os

try:
    import pyautogui
    print('a biblioteca pyautogui foi emportada com sucesso!')
except ImportError as k:
    print(f'Erro ao importar uma biblioteca: {k}')

try:
    import numpy
    print('a biblioteca 1 foi emportada com sucesso!')
except ImportError as a:
    print(f'Erro ao importar uma biblioteca: {a}')

try:
    import pandas as pd
    print('a biblioteca 2 foi emportada com sucesso!')
except ImportError as b:
    print(f'Erro ao importar uma biblioteca: {b}')

try:
    import matplotlib.pyplot as plt
    print('a biblioteca 3 foi emportada com sucesso!')
except ImportError as c:
    print(f'Erro ao importar uma biblioteca: {c}')

try:
    import seaborn as sns
    print('a biblioteca 4 foi emportada com sucesso!')
except ImportError as d:
    print(f'Erro ao importar uma biblioteca: {d}')

try:
    import sklearn
    print('a biblioteca 5 foi emportada com sucesso!')
except ImportError as e:
    print(f'Erro ao importar uma biblioteca: {e}')

try:
    import tensorflow as tf
    print('a biblioteca 6 foi emportada com sucesso!')
except ImportError as f:
    print(f'Erro ao importar uma biblioteca: {f}')

try:
    import torch
    print('a biblioteca 7 foi emportada com sucesso!')
except ImportError as g:
    print(f'Erro ao importar uma biblioteca: {g}')

try:
    import requests
    print('a biblioteca 8 foi emportada com sucesso!')
except ImportError as h:
    print(f'Erro ao importar uma biblioteca: {h}')

try:
    from bs4 import BeautifulSoup
    print('a biblioteca 9 foi emportada com sucesso!')
except ImportError as i:
    print(f'Erro ao importar uma biblioteca: {i}')

try:
    import flask
    print('Todas as bibliotecas foram emportadas com sucesso!')
except ImportError as j:
    print(f'Erro ao importar uma biblioteca: {j}')

os.system('pause')
os.system('cls')
