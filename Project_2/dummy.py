import tkinter as tk
from tkinter import *
from tkinter import ttk
from loginpage import *
from PIL import Image, ImageTk
from datetime import *
import io
import random
import mysql.connector as connector
con = connector.connect(host='localhost',
                        user='root',
                        password='1234A#stha',
                        database='food_ordering')

c_id=name
query="insert into orders("