{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:58:40.269701Z",
     "start_time": "2021-07-23T14:58:40.265713Z"
    }
   },
   "source": [
    "# Metode Pengujian"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Pengujian statistik yang dipilih untuk analisis ini adalah ANOVA (Analysis of Variance) karena tujuan dari analisis ini adalah untuk membandingkan pendapatan kotor setiap cabang toko (A, B, C).\n",
    "\n",
    "ANOVA dipilih karena memiliki beberapa kategori :\n",
    "1. Variabel kategori (Diskrit / Label)\n",
    "2. Variabel kontinu (Matematis / Numerik)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://www.analyticsvidhya.com/blog/2018/01/anova-analysis-of-variance/"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:44:59.856952Z",
     "start_time": "2021-07-23T14:44:59.852960Z"
    }
   },
   "source": [
    "# Import Library"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:07.341011Z",
     "start_time": "2021-07-29T22:23:05.214352Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import statsmodels.formula.api as smf\n",
    "import statsmodels.api as sm\n",
    "from scipy import stats\n",
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:45:06.033866Z",
     "start_time": "2021-07-23T14:45:06.028877Z"
    }
   },
   "source": [
    "# Load Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:07.383292Z",
     "start_time": "2021-07-29T22:23:07.341011Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>date_time</th>\n",
       "      <th>branch</th>\n",
       "      <th>city</th>\n",
       "      <th>customer_type</th>\n",
       "      <th>gender</th>\n",
       "      <th>product_line</th>\n",
       "      <th>payment</th>\n",
       "      <th>branch_location</th>\n",
       "      <th>unit_price</th>\n",
       "      <th>quantity</th>\n",
       "      <th>tax_5_percent</th>\n",
       "      <th>total</th>\n",
       "      <th>cogs</th>\n",
       "      <th>gross_margin_percentage</th>\n",
       "      <th>gross_income</th>\n",
       "      <th>rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2019-01-05 13:08:00</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Female</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>A - Yangon</td>\n",
       "      <td>74.69</td>\n",
       "      <td>7</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>548.9715</td>\n",
       "      <td>522.83</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>26.1415</td>\n",
       "      <td>9.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2019-03-08 10:29:00</td>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Female</td>\n",
       "      <td>Electronic accessories</td>\n",
       "      <td>Cash</td>\n",
       "      <td>C - Naypyitaw</td>\n",
       "      <td>15.28</td>\n",
       "      <td>5</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>80.2200</td>\n",
       "      <td>76.40</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>3.8200</td>\n",
       "      <td>9.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2019-03-03 13:23:00</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>Credit card</td>\n",
       "      <td>A - Yangon</td>\n",
       "      <td>46.33</td>\n",
       "      <td>7</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>340.5255</td>\n",
       "      <td>324.31</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>16.2155</td>\n",
       "      <td>7.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2019-01-27 20:33:00</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Male</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>A - Yangon</td>\n",
       "      <td>58.22</td>\n",
       "      <td>8</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>489.0480</td>\n",
       "      <td>465.76</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>23.2880</td>\n",
       "      <td>8.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2019-02-08 10:37:00</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Sports and travel</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>A - Yangon</td>\n",
       "      <td>86.31</td>\n",
       "      <td>7</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>634.3785</td>\n",
       "      <td>604.17</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>30.2085</td>\n",
       "      <td>5.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>2019-01-29 13:46:00</td>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Health and beauty</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>C - Naypyitaw</td>\n",
       "      <td>40.35</td>\n",
       "      <td>1</td>\n",
       "      <td>2.0175</td>\n",
       "      <td>42.3675</td>\n",
       "      <td>40.35</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>2.0175</td>\n",
       "      <td>6.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>2019-03-02 17:16:00</td>\n",
       "      <td>B</td>\n",
       "      <td>Mandalay</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Female</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>Ewallet</td>\n",
       "      <td>B - Mandalay</td>\n",
       "      <td>97.38</td>\n",
       "      <td>10</td>\n",
       "      <td>48.6900</td>\n",
       "      <td>1022.4900</td>\n",
       "      <td>973.80</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>48.6900</td>\n",
       "      <td>4.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>2019-02-09 13:22:00</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Male</td>\n",
       "      <td>Food and beverages</td>\n",
       "      <td>Cash</td>\n",
       "      <td>A - Yangon</td>\n",
       "      <td>31.84</td>\n",
       "      <td>1</td>\n",
       "      <td>1.5920</td>\n",
       "      <td>33.4320</td>\n",
       "      <td>31.84</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>1.5920</td>\n",
       "      <td>7.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>2019-02-22 15:33:00</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Normal</td>\n",
       "      <td>Male</td>\n",
       "      <td>Home and lifestyle</td>\n",
       "      <td>Cash</td>\n",
       "      <td>A - Yangon</td>\n",
       "      <td>65.82</td>\n",
       "      <td>1</td>\n",
       "      <td>3.2910</td>\n",
       "      <td>69.1110</td>\n",
       "      <td>65.82</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>3.2910</td>\n",
       "      <td>4.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>2019-02-18 13:28:00</td>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>Member</td>\n",
       "      <td>Female</td>\n",
       "      <td>Fashion accessories</td>\n",
       "      <td>Cash</td>\n",
       "      <td>A - Yangon</td>\n",
       "      <td>88.34</td>\n",
       "      <td>7</td>\n",
       "      <td>30.9190</td>\n",
       "      <td>649.2990</td>\n",
       "      <td>618.38</td>\n",
       "      <td>4.761905</td>\n",
       "      <td>30.9190</td>\n",
       "      <td>6.6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 16 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               date_time branch       city customer_type  gender  \\\n",
       "0    2019-01-05 13:08:00      A     Yangon        Member  Female   \n",
       "1    2019-03-08 10:29:00      C  Naypyitaw        Normal  Female   \n",
       "2    2019-03-03 13:23:00      A     Yangon        Normal    Male   \n",
       "3    2019-01-27 20:33:00      A     Yangon        Member    Male   \n",
       "4    2019-02-08 10:37:00      A     Yangon        Normal    Male   \n",
       "..                   ...    ...        ...           ...     ...   \n",
       "995  2019-01-29 13:46:00      C  Naypyitaw        Normal    Male   \n",
       "996  2019-03-02 17:16:00      B   Mandalay        Normal  Female   \n",
       "997  2019-02-09 13:22:00      A     Yangon        Member    Male   \n",
       "998  2019-02-22 15:33:00      A     Yangon        Normal    Male   \n",
       "999  2019-02-18 13:28:00      A     Yangon        Member  Female   \n",
       "\n",
       "               product_line      payment branch_location  unit_price  \\\n",
       "0         Health and beauty      Ewallet      A - Yangon       74.69   \n",
       "1    Electronic accessories         Cash   C - Naypyitaw       15.28   \n",
       "2        Home and lifestyle  Credit card      A - Yangon       46.33   \n",
       "3         Health and beauty      Ewallet      A - Yangon       58.22   \n",
       "4         Sports and travel      Ewallet      A - Yangon       86.31   \n",
       "..                      ...          ...             ...         ...   \n",
       "995       Health and beauty      Ewallet   C - Naypyitaw       40.35   \n",
       "996      Home and lifestyle      Ewallet    B - Mandalay       97.38   \n",
       "997      Food and beverages         Cash      A - Yangon       31.84   \n",
       "998      Home and lifestyle         Cash      A - Yangon       65.82   \n",
       "999     Fashion accessories         Cash      A - Yangon       88.34   \n",
       "\n",
       "     quantity  tax_5_percent      total    cogs  gross_margin_percentage  \\\n",
       "0           7        26.1415   548.9715  522.83                 4.761905   \n",
       "1           5         3.8200    80.2200   76.40                 4.761905   \n",
       "2           7        16.2155   340.5255  324.31                 4.761905   \n",
       "3           8        23.2880   489.0480  465.76                 4.761905   \n",
       "4           7        30.2085   634.3785  604.17                 4.761905   \n",
       "..        ...            ...        ...     ...                      ...   \n",
       "995         1         2.0175    42.3675   40.35                 4.761905   \n",
       "996        10        48.6900  1022.4900  973.80                 4.761905   \n",
       "997         1         1.5920    33.4320   31.84                 4.761905   \n",
       "998         1         3.2910    69.1110   65.82                 4.761905   \n",
       "999         7        30.9190   649.2990  618.38                 4.761905   \n",
       "\n",
       "     gross_income  rating  \n",
       "0         26.1415     9.1  \n",
       "1          3.8200     9.6  \n",
       "2         16.2155     7.4  \n",
       "3         23.2880     8.4  \n",
       "4         30.2085     5.3  \n",
       "..            ...     ...  \n",
       "995        2.0175     6.2  \n",
       "996       48.6900     4.4  \n",
       "997        1.5920     7.7  \n",
       "998        3.2910     4.1  \n",
       "999       30.9190     6.6  \n",
       "\n",
       "[1000 rows x 16 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"supermarket_sales_p.csv\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:07.392266Z",
     "start_time": "2021-07-29T22:23:07.385286Z"
    }
   },
   "outputs": [],
   "source": [
    "df_h = df[[\"branch_location\", \"gross_income\"]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:45:13.481338Z",
     "start_time": "2021-07-23T14:45:13.477348Z"
    }
   },
   "source": [
    "# Hipotesis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "α = 0.05 (Standart Hypothesis Test)\n",
    "- H0: Tidak ada perbedaan yang signifikan antara rata-rata gross income diantara 3 toko.\n",
    "- H1: Ada perbedaan yang signifikan antara rata-rata gross income dari minimal 2 toko."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:45:25.655930Z",
     "start_time": "2021-07-23T14:45:25.652937Z"
    }
   },
   "source": [
    "# Distribution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:07.652570Z",
     "start_time": "2021-07-29T22:23:07.394260Z"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsgAAAHmCAYAAABu5XitAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAAsTAAALEwEAmpwYAAAhSElEQVR4nO3df7zld10f+NfbmRBSfiM4puIyVClMiJDqgIBR7xB1qWihXQpM1c3SWbLxUQMs3ZrArLpsnUeT7pbaIpJNGGts7QAVIixxUzDMFaI0QCCRhNEVQlhBMIIQCIY0Gd77xzkDnwzz48zMPffcufN8Ph7ncc/38/2e7/d9557P3Nf9nM/3+63uDgAAMPEtiy4AAADWEgEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGCwcdEFzOJRj3pUb968edFlcBy+8pWv5EEPetCiy4BThj4Hq0+/O3ndeOONn+vuRx/cflIE5M2bN+eDH/zgosvgOCwvL2dpaWnRZcApQ5+D1affnbyq6pOHajfFAgAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGGyc586r6vYkX06yP8l93b21qh6Z5E1JNie5PckLuvsL86wDAABmtRojyNu6+5zu3jpdviTJdd39+CTXTZcBAGBNWMQUi+cmuWr6/Kokz1tADQAAcEjzDsid5J1VdWNVXTBt29Tdn5k+/2ySTXOuAQAAZjbXOchJzu3uT1fVtyV5V1X98biyu7uq+lAvnAbqC5Jk06ZNWV5ennOpzMNdd93lZwerSJ+D1affrT9zDcjd/enp1zuq6uokT0vyF1V1Znd/pqrOTHLHYV57RZIrkmTr1q29tLQ0z1KZk+Xl5fjZwerR52D16Xfrz9ymWFTVg6rqIQeeJ/mxJLckeXuS86ebnZ/kbfOqgcXZs2dPzj777Jx33nk5++yzs2fPnkWXBAAwk3mOIG9KcnVVHTjOf+zua6vqA0neXFU7knwyyQvmWAMLsGfPnuzcuTO7d+/O/v37s2HDhuzYsSNJsn379gVXBwDfMM0pC9d9yBmnLMjcRpC7+7bufsr08aTu3jVt/3x3n9fdj+/uH+nuv5pXDSzGrl27snv37mzbti0bN27Mtm3bsnv37uzatWvRpQHA/XT3CT8ee/E7TngfrC3upMeK27dvX84999z7tZ177rnZt2/fgioCAJidgMyK27JlS66//vr7tV1//fXZsmXLgioCAJidgMyK27lzZ3bs2JG9e/fmvvvuy969e7Njx47s3Llz0aUBABzVvK+DzCnowIl4F110Ufbt25ctW7Zk165dTtCDObroooty5ZVX5p577snpp5+el7zkJXnta1+76LIATkoCMnOxffv2bN++3bUhYRVcdNFFufzyy3PZZZflrLPOykc/+tFcfPHFSSIkAxwHUywATnJXXnllLrvssrziFa/IAx/4wLziFa/IZZddliuvvHLRpQGclARkgJPcPffckwsvvPB+bRdeeGHuueeeBVUEcHITkAFOcqeffnouv/zy+7VdfvnlOf300xdUEcDJzRxkgJPcS17ykq/POT7rrLPymte8JhdffPE3jSoDMBsBGeAkd+BEvFe96lVfv4rFhRde6AQ9gONkigXAOvDa1742X/3qV7N379589atfFY4BToCADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGTmYs+ePTn77LNz3nnn5eyzz86ePXsWXRIAwEw2LroA1p89e/Zk586d2b17d/bv358NGzZkx44dSZLt27cvuDoAgCMzgsyK27VrV3bv3p1t27Zl48aN2bZtW3bv3p1du3YtujQAgKMSkFlx+/bty7nnnnu/tnPPPTf79u1bUEUAALMTkFlxW7ZsyfXXX3+/tuuvvz5btmxZUEUAALMTkFlxO3fuzI4dO7J3797cd9992bt3b3bs2JGdO3cuujQAgKNykh4r7sCJeBdddFH27duXLVu2ZNeuXU7QgxlU1aJLSJJ096JLAFgYI8jMxfbt23PLLbfkuuuuyy233CIcw4y6+4Qej734HSe8D+EYONUJyAAAMBCQAQBgICADAMDASXoclpOFAIBTkRFkDmslTvRZiROGAABWk4AMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYDD3gFxVG6rqw1X1juny46rqhqr6WFW9qaoeMO8aAABgVqsxgvyyJPuG5cuS/Ovu/u4kX0iyYxVqAACAmcw1IFfVY5I8J8kbpsuV5FlJfnu6yVVJnjfPGgAA4FjMewT5V5L8fJKvTZe/NckXu/u+6fKnknzHnGsAAICZbZzXjqvqJ5Lc0d03VtXScbz+giQXJMmmTZuyvLy8ovWxevzsYHXpc7D69Lv1ZW4BOckPJPl7VfXjSR6Y5KFJ/k2Sh1fVxuko8mOSfPpQL+7uK5JckSRbt27tpaWlOZbK3Fx7TfzsYBXpc7D69Lt1Z25TLLr7ld39mO7enORFSd7d3T+VZG+S5083Oz/J2+ZVAwAAHKtFXAf54iSvqKqPZTInefcCagAAgEOa5xSLr+vu5STL0+e3JXnaahwXAACOlTvpAQDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYDC3gFxVD6yq91fVzVV1a1W9etr+uKq6oao+VlVvqqoHzKsGAAA4VvMcQb4nybO6+ylJzkny7Kp6epLLkvzr7v7uJF9IsmOONQAAwDGZW0Duibumi6dNH53kWUl+e9p+VZLnzasGAAA4VnOdg1xVG6rqpiR3JHlXko8n+WJ33zfd5FNJvmOeNQAAwLHYOM+dd/f+JOdU1cOTXJ3kibO+tqouSHJBkmzatCnLy8vzKJFV4GcHq0ufg9Wn360vcw3IB3T3F6tqb5JnJHl4VW2cjiI/JsmnD/OaK5JckSRbt27tpaWl1SiVlXbtNfGzg1Wkz8Hq0+/WnXlexeLR05HjVNUZSX40yb4ke5M8f7rZ+UneNq8aAADgWM1zBPnMJFdV1YZMgvibu/sdVfXRJG+sql9O8uEku+dYAwAAHJO5BeTu/qMkf+cQ7bcledq8jgsAACfCnfQAAGAgIAMAwGCmgFxVZ1TVE+ZdDAAALNpRA3JV/WSSm5JcO10+p6rePue6AABgIWYZQf7fMjmp7otJ0t03JXnc3CoCAIAFmiUg39vddx7U1vMoBgAAFm2Wy7zdWlX/KMmGqnp8kpcm+cP5lgUAAIsxywjyRUmelOSeJHuSfCnJy+dYEwAALMxRR5C7+6+T7Jw+AABgXTtqQK6qrUlelWTzuH13P3l+ZQEAwGLMMgf5t5L8syQfSfK1+ZYDAACLNUtA/svudt1jAABOCbME5F+qqjckuS6TE/WSJN391rlVBQAACzJLQH5xkicmOS3fmGLRSQRkAADWnVkC8lO7+wlzrwQAANaAWa6D/IdVddbcKwEAgDVglhHkpye5qao+kckc5ErSLvMGAMB6NEtAfvbcqwAAgDXiqFMsuvuTSR6e5Cenj4dP2wAAYN05akCuqpdlcrOQb5s+/kNVXTTvwgAAYBFmmWKxI8n3d/dXkqSqLkvyviSvnWdhAACwCLNcxaKS7B+W90/bAABg3ZllBPnfJbmhqq6eLj8vye65VQQAAAt01IDc3a+pquUk506bXtzdH55rVQAAsCBHDchV9fQkt3b3h6bLD62q7+/uG+ZeHQAArLJZ5iC/Psldw/Jd0zYAAFh3ZjpJr7v7wEJ3fy2zzV0GAICTziwB+baqemlVnTZ9vCzJbfMuDAAAFmGWgHxhkmcm+XSSTyX5/iQXzLMoAABYlFmuYnFHkhetQi0AALBws1zF4tFJXpJk87h9d//j+ZUFAACLMcvJdm9L8t4kv5f731EPAADWnVkC8t/o7ovnXgkAAKwBs5yk946q+vG5VwIAAGvALAH5ZZmE5Lur6ktV9eWq+tK8CwMAgEWY5SoWD1mNQgAAYC04bECuqu890gu7+0MrXw4AACzWkUaQ/9UR1nWSZ61wLQAAsHCHDcjdvW01CwEAgLVglpP0AADglCEgAwDAQEAGAIDBUQNyVf1AVT1o+vynq+o1VfXY+ZcGAACrb5YR5Ncn+euqekqSf5rk40l+c65VAQDAgswSkO/r7k7y3CS/2t2vS+LmIQAArEtHvZNeki9X1SuT/HSSH6qqb0ly2nzLAgCAxZhlBPmFSe5JsqO7P5vkMUn+j7lWBQAACzLTCHKSf9Pd+6vqbyd5YpI98y0LAODonvLqd+bOu+9ddBnZfMk1Cz3+w844LTf/0o8ttIb1ZJaA/J4kP1hVj0jyziQfyGRU+afmWRgAwNHcefe9uf3S5yy0huXl5SwtLS20hkUH9PVmlikW1d1/neQfJPm17v6HSc6eb1kAALAYMwXkqnpGJiPGB/48cYMRAADWpVmC7suTvDLJ1d19a1X9rSR751oVAAAsyFHnIHf37yf5/ap6cFU9uLtvS/LS+ZcGAACrb5ZbTX9PVX04ya1JPlpVN1bVk+ZfGgAArL5Zplj8X0le0d2P7e7/JpPbTV8537IAAGAxZgnID+rur8857u7lJA+aW0UAALBAs1wH+baq+oUk/366/NNJbptfSQAAsDizjCD/4ySPTvLWJG9J8qhpGwAArDtHHEGuqg1J3trd21apHgAAWKgjBuTu3l9VX6uqh3X3natVFMDJ6CmvfmfuvPveRZex8FvOPuyM03LzL/3YQmsAOBGzzEG+K8lHqupdSb5yoLG7XQsZYHDn3ffm9kufs9AalpeXs7S0tNAaFh3QAU7ULAH5rdMHAACse7PcSe+q1SiElbVWPupNFj+a5ONeAOBYHDYgV9Vzkzymu183Xb4hk6tZJMnPd/dvr0J9HKe18FFv4uNeAODkc6TLvP18krcPy6cneWqSpSQ/O8eaAABgYY40xeIB3f1nw/L13f35JJ+vKnfSAwBgXTrSCPIjxoXu/rlh8dEBAIB16EgB+YaqesnBjVX1PyV5//xKAgCAxTnSFIv/OcnvVNU/SvKhadv3ZTIX+XlzrgsAABbisAG5u+9I8syqelaSJ02br+nud69KZQAAsACzXAf53UmEYgAATglHmoMMAACnHAEZAAAGcwvIVfWdVbW3qj5aVbdW1cum7Y+sqndV1Z9Ovz7iaPsCAIDVMs8R5PuS/NPuPivJ05P8k6o6K8klSa7r7scnuW66DAAAa8LcAnJ3f6a7PzR9/uUk+5J8R5LnJrlqutlVcck4AADWkFWZg1xVm5P8nSQ3JNnU3Z+Zrvpskk2rUQMAAMziqJd5O1FV9eAkb0ny8u7+UlV9fV13d1X1YV53QZILkmTTpk1ZXl6ed6nrzlr4N7vrrrvWRB1roQZODYt+r+lznIoW/X7T79afuQbkqjotk3D8W9391mnzX1TVmd39mao6M8kdh3ptd1+R5Iok2bp1ay8tLc2z1PXn2muyFv7NlpeXF1/HGvm34BSwBt5r+hynnDXwftPv1p95XsWikuxOsq+7XzOsenuS86fPz0/ytnnVAAAAx2qeI8g/kORnknykqm6atr0qyaVJ3lxVO5J8MskL5lgDAAAck7kF5O6+PkkdZvV58zouAACcCHfSAwCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYbFx0AQAAx+shWy7J91x1yaLLSK5a7OEfsiVJnrPYItYRARkAOGl9ed+luf3SxQbD5eXlLC0tLbSGzZdcs9DjrzemWAAAwEBABgCAgYAMAAADARkAAAYCMgAADFzFAmCFuNzUhMtNASc7ARlghbjc1ITLTQEnO1MsAABgICADAMDAFIt1as3MhUzMhwQATioC8jq1FuZCJuZDAgAnH1MsAABgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAzmFpCr6ter6o6qumVoe2RVvauq/nT69RHzOj4AAByPeY4g/0aSZx/UdkmS67r78Umumy4DAMCaMbeA3N3vSfJXBzU/N9+4r9pVSZ43r+MDAMDxWO05yJu6+zPT559NsmmVjw8AAEe0sFtNd3dXVR9ufVVdkOSCJNm0aVOWl5dXq7R1Yy38m911111roo61UAOnhkW/1/Q5TkWLfr/pd+vPagfkv6iqM7v7M1V1ZpI7Drdhd1+R5Iok2bp1ay8tLa1SievEtddkLfybLS8vL76ONfJvwSlgDbzX9DlOOWvg/abfrT+rPcXi7UnOnz4/P8nbVvn4AABwRPO8zNueJO9L8oSq+lRV7UhyaZIfrao/TfIj02UAAFgz5jbForu3H2bVefM6JgAAnCh30gMAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBg46ILYH42X3LNokuYuHaxdTzsjNMWenwA4OQiIK9Tt1/6nEWXkGQS0tdKLQAAszDFAgAABgIyAAAMBGQAABgIyAAAMHCSHsAKWhNXj3HlGE4x+p1+t9IEZIAVshau2OLKMZxq1sL7Xb9bf0yxAACAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAGAjIAAAwEZAAAGAjIAAAwEJABAGAgIAMAwEBABgCAgYAMAAADARkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMNi46AIA+IaqOvF9XHbidXT3ie8E4CRlBBlgDenuE3rs3bv3hPchHAOnOiPIHNZKjGQlJz6a5Zc1ALCaFjKCXFXPrqo/qaqPVdUli6iBo1uJUaiVGM0CgHmpqhN+fPKynzjhfbC2rHpArqoNSV6X5O8mOSvJ9qo6a7XrAAAwGMShLGIE+WlJPtbdt3X3f03yxiTPXUAdAADwTRYRkL8jyZ8Ny5+atgEAwMKt2ZP0quqCJBckyaZNm7K8vLzYgjgud911l58drCJ9Dlaffrf+LCIgfzrJdw7Lj5m23U93X5HkiiTZunVrLy0trUpxrKzl5eX42cHq0edg9el3688iplh8IMnjq+pxVfWAJC9K8vYF1AEAAN9k1UeQu/u+qvq5JP85yYYkv97dt652HQAAcCgLmYPc3b+b5HcXcWwAADgSt5oGAICBgAwAAAMBGQAABgIyAAAMBGQAABgIyAAAMBCQAQBgICADAMBAQAYAgIGADAAAAwEZAAAG1d2LruGoquovk3xy0XVwXB6V5HOLLgJOIfocrD797uT12O5+9MGNJ0VA5uRVVR/s7q2LrgNOFfocrD79bv0xxQIAAAYCMgAADARk5u2KRRcApxh9DlaffrfOmIMMAAADI8gAADAQkE9hVfW8quqqeuIxvu7bqur2qvr2oe11VfXKla8STj5Vtb+qbqqqm6vqQ1X1zGN8/dK0b/6PQ9s507b/ZYVq/I2qev6JbgOLVFXfXlVvrKqPV9WNVfW7VfW3j+H1B/raTw5t76iqpXnUe4jj/+9V9SPT5y+vqr+xGsfl6ATkU9v2JNdPv86su+9IcmmS/zNJqup7k/zggWUgd3f3Od39lCSvTPIvjmMftyR5wbC8PcnNK1EcrAdVVUmuTrLc3d/V3d+XSX/bdIy7+lSSnStd3yy6+xe7+/emiy9PIiCvEQLyKaqqHpzk3CQ7krzoOHZxRZLvqqptSV6X5OeS/A9V9YHpqNlbDvwlPB2F+rdV9YdVdduBEamq+paq+rWq+uOqetf0L/8D686rqg9X1Ueq6ter6vRp++1V9erpqNxHjnX0GxbgoUm+cByv+2SSB1bVpmkQeHaS/+fAyqp6yTH2t6qqX62qP6mq30vybcO+fnG6r1uq6orp8e7nUNtU1XdV1YeGbR4/LsOcbUtyb3dffqChu2/u7vce435uTnJnVf3owSuO9X0//R31L6e/n95fVd9dVQ+pqk9U1WnTbR56YPnApzRV9dIkfzPJ3qraO93u9VX1waq6tapePW17alW9dfr8uVV1d1U9oKoeWFW3HeP3zREIyKeu5ya5trv/3ySfr6rvO5YXd/fXkvxskrck+ZPufk+St3b3U6ejZvsyCd8HnJlJIP+JTEafk+QfJNmc5KwkP5PkGUlSVQ9M8htJXtjd35Nk4/RYB3yuu783yeuTrMjHzbDCzqjJFIs/TvKGJP/8OPfz20n+YZJnJvlQknuGdcfa3/5+kidk0t/+++k+D/jV6b7OTnLG9HUH+6ZtuvvjmQSLc6bbvDjJvzvO7xWO1dlJblyhfe1K8r8eov143vd3Tn93/WqSX+nuLydZTvKc6foXZdJ/7z3wgu7+t0n+PMm27t42bd45vfnIk5P8cFU9OcmHkxw47g9m8knTU5N8f5IbjvN75xAE5FPX9iRvnD5/Y45xmkWSdPdNmXTOX5s2nV1V762qjyT5qSRPGjb/ne7+Wnd/NN/4+OvcJP9p2v7ZJHun7U9I8olpeE+Sq5L80LCvt06/3phJwIa15sAUiydmMvL7m4calZ3BmzMJyNuT7Dlo3bH2tx9Ksqe793f3nyd597D9tqq6YbqvZx20r6Nt84YkL66qDUlemOQ/Hsf3CQs1HeRJVZ170Krjed/vGb4+Y9x++nzWPyRfMB2Z/vD0uGd1931JPl5VW5I8LclrMunbP5jkWEfOOQIB+RRUVY/MpKO/oapuT/LPMumIddB2/2Q6CnZTVf3Nw+zua9NHMhn1/bnpX86vTvLAYbtx5Ot4gsLowL72ZzK6DGtWd78vyaOSPHpsn6V/Tf9wvDfJjya57qDVv5EV6G/TT2x+Lcnzp/u68qB9HW2btyT5u5mMOt/Y3Z8/0vFgBd2a5Kiffs74uyw5aBT5BN73ffDz7v6DJJtrcvLfhu6+5Sg1Py6TT0jP6+4nJ7lmOPZ7pse+N8nvZTLYdG4E5BUlIJ+anp/k33f3Y7t7c3d/Z5JPZPIX6Nd19+umo2DnTEecjuYhST4znWf1UzNs/wdJ/ruazEXelGRp2v4nmfxH8t3T5Z9J8vsz7A/WnJrMk9+Q5H7B8Rj61y8mubi79x/Ufqz97T1JXlhVG6rqzEzmbybf+KX7uZqcm3Coq1Ycdpvu/mqS/5zJlCfTK1hN705yelVdcKChqp5cVcf1u6y735nkEZlMaUiO/33/wuHr+4b238xkpPlw/eTLmfTrZHLuwlcymcqxKZNAfMB7Mzmh733d/ZdJvjWTT16PGLo5NkbfTk3bk1x2UNtbpu3vOYH9/kImc6D+cvr1IUfePG9Jcl6Sjyb5s0zmWN7Z3V+tqhcn+U9VtTHJB5JcfvjdwJpzRlXdNH1eSc4/RMCdSXf/4WFWHWt/uzqTT44+muT/y/QXd3d/saquzOSX62cz6W8H13C0bX4rkznO75zhW4IV0d1dVX8/ya9U1cVJvprk9kzC4/HaleRt0/0f7/v+EVX1R5l8krP9oO1/Od88XeqAK5JcW1V/3t3bqurDSf44k9+PfzBsd0MmU6cO/L7+oyTf3u78tqLcSY+FqqoHd/ddVfWtSd6f5AemHysDJ4maXJv5Yd39C4uuBVbLod7302mLW7v7c4fY/vlJntvdP7N6VXK8jCCzaO+oqocneUCSfy4cw8mlqq5O8l2ZjE7DKeFY3/dV9dpMpkn8+DzrYuUYQQYAgIGT9AAAYCAgAwDAQEAGAICBgAywhlTV/ukNDW6uqg9V1TOP/qoTOt7mqnL9VICBq1gArC13d/c5SVJV/22Sf5Hkh8cNqmrj9JazAMyBEWSAteuhSb6QJFW1VFXvraq3Z3Kzj1TV71TVjVV160F3E7urqnZNR6H/y/ROXKmqTVV19bT95mF0ekNVXTndzzur6oxV/j4B1hSXeQNYQ6pqf5KPZHKb2zOTPKu7b6yqpSTXJDm7uz8x3faR3f1X00D7gSQ/3N2fr6pO8ve6+/+uqn+Z5Evd/ctV9aZMbk/7K1W1IcmDM7m17scyubnBTVX15iRv7+7/sLrfOcDaYQQZYG25u7vP6e4nJnl2kt+sqpque/+BcDz10qq6Ocl/SfKdSR4/bf+vSd4xfX5jks3T589K8vok6e793X3ntP0T3X3TIbYHOCWZgwywRnX3+6rqUUkePW36yoF10xHlH0nyjO7+66pazmTUOUnu7W98PLg/R/+//p7h+f4kplgApzQjyABrVFU9McmGJJ8/xOqHJfnCNBw/McnTZ9jldUl+drrvDVX1sBUrFmAdEZAB1pYzppd5uynJm5Kc3937D7HdtUk2VtW+JJdmMs3iaF6WZFtVfSSTqRRnrVDNAOuKk/QAAGBgBBkAAAYCMgAADARkAAAYCMgAADAQkAEAYCAgAwDAQEAGAICBgAwAAIP/HyQCmuTlkzXIAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 720x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = df_h.boxplot(by=\"branch_location\", column=\"gross_income\", figsize=(10, 7))\n",
    "ax.set_xlabel(\"Branch\")\n",
    "ax.set_ylabel(\"Gross Income\")\n",
    "plt.suptitle('')\n",
    "plt.title('')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:07.659551Z",
     "start_time": "2021-07-29T22:23:07.653567Z"
    }
   },
   "outputs": [],
   "source": [
    "df_h = df[[\"branch_location\", \"gross_income\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:07.671518Z",
     "start_time": "2021-07-29T22:23:07.661545Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  branch_location  gross_income\n",
      "0      A - Yangon       26.1415\n",
      "1   C - Naypyitaw        3.8200\n",
      "2      A - Yangon       16.2155\n",
      "3      A - Yangon       23.2880\n",
      "4      A - Yangon       30.2085\n"
     ]
    }
   ],
   "source": [
    "print(df_h.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:45:37.655991Z",
     "start_time": "2021-07-23T14:45:37.652003Z"
    }
   },
   "source": [
    "# Permutation Test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:07.697457Z",
     "start_time": "2021-07-29T22:23:07.673513Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Observed means: [14.87400147 15.2320241  16.05236738]\n",
      "Variance: 0.3649482520363527\n",
      "0.39588895932158713\n"
     ]
    }
   ],
   "source": [
    "observed_variance = df_h.groupby(\"branch_location\").mean().var()[0]\n",
    "print(\"Observed means:\", df_h.groupby(\"branch_location\").mean().values.ravel())\n",
    "print(\"Variance:\", observed_variance)\n",
    "def perm_test(df_input):\n",
    "    df_input = df_input.copy()\n",
    "    df_input[\"gross_income\"] = np.random.permutation(df_input[\"gross_income\"].values)\n",
    "    return df_input.groupby(\"branch_location\").mean().var()[0]\n",
    "\n",
    "print(perm_test(df_h))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:12.369821Z",
     "start_time": "2021-07-29T22:23:07.700442Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pr(Prob) 0.403\n"
     ]
    },
    {
     "data": {
      "image/png": "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ycZJnqi1frGUsm0pZdda638NVDBom/F1fNMRAAAAelZX18AopUxJcmaSD3U2bZjkXwYqFAAAAMDyur2I5zFJjkryVJLUWucl2WygQgEAAAAsr9slJL+vtdZSSk2SUsomA5gJWmn2uNlJkr45fWv1uKNHj87cuXPX6jF7zahRo3Lfffc1HQMAABhA3RYYV5RSLk6yZSnl3UnekeSSgYsF7fPkbU8OyHHnzp2bWuuAHLtXlFKajgAAAAywNRYYZelfBjOS/GmSJ5KMSXJOrfX6Ac4GAAAAkKSLAqOzdOTaWuurkygtAAAAgEHX7UU8byul7DWgSQAAAACeR7cFxj5Jbi6l/N9Sys9KKT8vpfxsIIMBSa0106dPzz777JNNN900m2++eQ444IBcddVVK4wbP358jj322IZSDrw77rgjpZTMmjWr6SgAAEBDXrDAKKW8vPPwsCR/kuSgJEcmOaLzHRhA733ve/Oud70r++yzT771rW9lxowZGT16dCZNmpTzzz+/6XgAAACDZk3XwPh2krG11rmllG/WWv/HIGSCVtrh3TsM6vt9+9vfzuc///lcdNFFec973tO//fDDD8/222+fD3/4wzn00EMzduzYQc21skWLFmXEiBGNZgAAANZ/a1pCsvy9Cf9kIINA242ZNiZjpo0ZtPf753/+5+y2225597vfvcq+D3/4w9lss83y2c9+doXt06ZNy+jRozNixIhMnDgxDz744Ar7/+Ef/iG77bZbhg8fnpEjR2bChAl56KGH+vc//vjjmTx5ckaOHJnhw4dn//33zy233LLCMUop+dSnPpX3v//92XbbbfPqV786U6dOzfbbb5/nnntuhbHXXHNNSim59957+7ddeuml2XPPPTNs2LCMGjUq//iP/7jKz/e5z30uu+yySzbZZJMceeSRmT9/fve/OAAAYL20pgKjPs9jYAAtXrw4N910U4488sgMGTJklf1bbLFFDjzwwPz4xz/u33bTTTflM5/5TD71qU/lsssuy89+9rMcffTR/fu/9KUv5eMf/3g+8IEP5Hvf+14uuuii7LbbbnnqqaeSJM8++2wOOeSQ/OAHP8gnPvGJfPvb3862226bQw45ZIWSI0k+8YlPZP78+fnyl7+cT3/60zn++OPz8MMP58Ybb1xh3IwZMzJu3Ljstttu/a879dRTc/TRR+fqq6/Oqaeemo985CMrFDEzZ87MaaedliOOOCJXXnllXv3qV+cd73jHH/07BQAA1m1rWkLy2lLKE1k6E2NE53E6z2utdfMBTQctsnDOwiTJZuM2G/D3evTRR/Pss89m1KhRzztm1KhRue666/qfP/LII7npppvy8pe/vH//G97whlx33XWZMGFCbr311rzpTW/Ke9/73v7XvOUtb+l//C//8i+54447cuedd2b33XdPkhxyyCEZM2ZMLrjggnziE5/oH7vDDjtkxowZK+R5zWtekxkzZuTAAw9MsrQQmTlzZj7ykY8kSZ544omce+65OfvsszNlypQkyaGHHpqnn346f//3f59TTz01Q4YMycc+9rFMmDAhF110UZLksMMOy4IFC3LppZe++F8kAACw3njBGRi11iG11s1rrZvVWod2Hi97rrygp8zpm5M5fXOajvG8xo4d219eJMnrX//6bLfddrn11luTJK973ety7bXXZsqUKbn11luzZMmSFV7/gx/8IOPGjcuuu+6axYsXZ/HixUmSAw44ILNnz15h7Jvf/OZV3v/444/PN7/5zf7Xffe7383ChQvz1re+NcnSGSJPPfVUjjvuuP7jL168OAcddFAefvjhPPDAA1m8eHFuu+22TJo0aYVjL1+0AAAAvanb26gCg2ibbbbJsGHDMnfu3OcdM3fu3Oy00079z7fbbrtVxmy33Xb91494xzvekY9//OO54oorss8++2TkyJE5++yz+4uMRx99NDfffHM23HDDFb6++MUv5v7771/huCNHjlzlvY4//vg8+uij+dGPfpRk6fKR/fbbr79UefTRR5Mke+655wrHXzZj4/7778+jjz6aJUuWrPKzrO5nAwAAesualpAADRg6dGj222+/XHPNNfnkJz+ZDTZYsWt84oknMmvWrBxzzDH92x555JFVjvPII49khx2W3j1lgw02yBlnnJEzzjgj999/f77yla/kb//2b7PzzjvnPe95T7baaqv09fX1L91Y3rBhw1Z4XkpZZcwrXvGK9PX1ZcaMGXnDG96Q73znO/n4xz/ev3+rrbZKklx99dWrLUDGjBmTESNGZMiQIav8LKv72QAAgN6iwICWet/73pdjjjkml156aSZPnrzCvvPOOy9PPPFETj/99P5tt912W37961/3z3j4yU9+kkceeSR77733KsfeZZddctZZZ+WLX/xifvGLXyRJDj744Hz/+9/Py1/+8pc84+GEE07Ixz72sRx00EFZtGhRjjvuuP59++23X0aMGJF58+Zl4sSJz3uMP/uzP8vMmTNXuHXslVde+ZLyAAAA6w8FBrTU0Ucfnfe85z057bTT8otf/CJHHHFEFi9enBkzZmT69On5h3/4h4wdO7Z//LbbbpuJEyfm3HPPzTPPPJMzzzwzY8eOzYQJE5Ikp5xySrbaaqvsu+++2WKLLXLDDTfknnvuyfnnn58kefvb357Pf/7zGT9+fP76r/86f/Inf5LHHnsst956a7bffvucccYZa8z81re+NX/zN3+Tv/mbv8kb3/jG/tkfSbLllltm6tSped/73pe5c+fmjW98Y5577rncfffdueGGG/Ktb30rydJbxL7lLW/JqaeemmOOOSY33njjChcrBQAAepMCA1rsc5/7XPbZZ59cdNFFueSSS7LBBhtk7NixmTlzZo466qgVxu6///455JBD8v73vz8LFizI+PHjM23atP79++23Xy655JJcfPHFeeaZZ7Lbbrvlkksu6b/V6vDhw3PDDTfknHPOyZQpU/Lwww9nu+22y957773Kez2fXXbZJfvvv39+8pOf9N9pZHkf/OAHs+OOO+bCCy/MBRdckOHDh2ePPfbI8ccf3z/mmGOOyWc+85mcd955ufzyyzN+/PhcdtllOeyww17CbxAAAFhflFpr0xnWur6+vrryXRPWBaPPuqbpCF2577xVp/+vC9lXl/vFmFVmJUnG1/F/fJjllFKyPv53OJj8DgEAYP1RSplTa+1bebsZGNClcbPHNR0BAACgZykwoEubjdus6QgAAAA9a4M1DwEAAABolgIDunTX5Lty1+S7mo4BAADQkywhoae9mIuPTr9kkyTJYVvdO1BxBsWsWbNy4IEH5uc//3le9apXNR0HAACgK2ZgQI8ZO3ZsbrrpprziFa9oOgoAAEDXzMCAHlFrzbPPPpvNN988++67b9NxAAAAXhQzMKBlpk+fno022ii//e1vV9h+5513ppSSH/zgB7nmmmty6KGHZrvttusvJL7//e+vMH7q1KnZZptt8m//9m/Za6+9Mnz48Hz961/PrFmzUkrJHXfc0T/2ggsuyF577ZUtttgiI0eOzJFHHpl7711xqcz48eNz7LHH5qtf/Wp22223bL755jn88MPzwAMPrDBu0aJF+eAHP5hRo0Zl2LBh2XXXXfOhD31ohTGXXnpp9txzzwwbNiyjRo3KP/7jP66F3xwAALA+U2BAyxx99NEppeRb3/rWCttnzJiRkSNH5sADD8x//dd/5cgjj8yXv/zlfPOb38z++++fww8/PD/5yU9WeM3TTz+dE088Me9617ty3XXXZe+9917tez7wwAM5/fTTM3PmzFxyySVZsmRJ9t9///zud79bYdwtt9ySz372s7ngggsybdq03HbbbZk8eXL//lprJk2alIsuuiinnXZarr322px77rl59NFH+8d84hOfyKmnnpqjjz46V199dU499dR85CMfyWc/+9k/9lcHAACsxywhgZbZcsstM2HChMyYMSMnn3xy//YZM2bk2GOPzZAhQ3L66af3b3/uuedy4IEH5s4778xll12W17/+9f37Fi1alE996lOZNGlS/7b58+ev8p4XXnhh/+MlS5b0z+6YOXNm3v72t/fve+KJJ3LNNdfkZS97WZLkoYceyhlnnJFFixZlxIgR+f73v5/rr78+M2fOzFFHHdX/umXHeOKJJ3Luuefm7LPPzpQpU5Ikhx56aJ5++un8/d//fU499dQMGTLkJf/uAACA9ZcZGNCl+0YuyX0jlwzKex1//PH54Q9/mMceeyxJcvvtt+fuu+/O8ccfn2TpjIkTTzwxO+20U4YOHZoNN9ww3//+93P33XevcJxSSg4//PA1vt/NN9+cQw89NFtvvXWGDh2ajTfeOE8++eQqx9trr736y4skeeUrX5kkefDBB5MkP/rRj7LVVlutUF4s76abbspTTz2V4447LosXL+7/Ouigg/Lwww+vshwFAABgGTMwoEtTT3pm0N7rqKOOyoYbbphvfvObmTx5cmbMmJGdd945b3jDG/Lcc8/lqKOOysKFC/PRj340u+22WzbZZJOcc845eeSRR1Y4zste9rJstNFGL/hev/71r/OmN70pe++9dy6++OLsuOOO2WijjTJx4sQ888yKP/OWW265wvNlx1427rHHHssOO+zwvO+1bCnJnnvuudr9999/f0aNGvWCeQEAgN7UWIFRShmSZHaSB2utR5RSdk3yr0m2TjInyV/WWn9fShmW5EtJxiV5LMnxtdb7GooNg2LTTTfNxIkTM2PGjEyePDlXXHFFjjvuuJRScs899+Q//uM/8t3vfjcTJkzof82iRYtW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",
      "text/plain": [
       "<Figure size 1080x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "random.seed(1)\n",
    "perm_variance = [perm_test(df_h) for _ in range(3000)]\n",
    "print('Pr(Prob)', np.mean([var > observed_variance for var in perm_variance]))\n",
    "\n",
    "fig, ax = plt.subplots(figsize=(15, 7))\n",
    "ax.hist(perm_variance, bins=20, rwidth=0.9)\n",
    "ax.axvline(x = observed_variance, color='m', lw=2, linestyle=\"--\")\n",
    "ax.text(0.45, 400, 'Observed\\nvariance', bbox={'facecolor':'white'}, fontsize=15)\n",
    "ax.set_xlabel('Variance')\n",
    "ax.set_ylabel('Frequency')\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:12.396794Z",
     "start_time": "2021-07-29T22:23:12.371815Z"
    }
   },
   "outputs": [],
   "source": [
    "df = pd.DataFrame(perm_variance, columns=[\"column\"])\n",
    "df.to_csv('perm_variance.csv', index = False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:46:14.632896Z",
     "start_time": "2021-07-23T14:46:14.627909Z"
    }
   },
   "source": [
    "## Conclusion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:37:58.189640Z",
     "start_time": "2021-07-23T14:37:58.183654Z"
    }
   },
   "source": [
    "Karena probabilitas dari observed value > α = 0.05, we can't reject H0 which means:\n",
    "- There's no significant differences between means of gross income of each branch."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:46:39.130059Z",
     "start_time": "2021-07-23T14:46:39.126071Z"
    }
   },
   "source": [
    "# F - Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:12.442626Z",
     "start_time": "2021-07-29T22:23:12.400739Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wall time: 130 ms\n",
      "Wall time: 8 ms\n",
      "                    df         sum_sq     mean_sq         F   PR(>F)\n",
      "branch_location    2.0     242.602644  121.301322  0.884583  0.41321\n",
      "Residual         997.0  136716.894906  137.128280       NaN      NaN\n"
     ]
    }
   ],
   "source": [
    "%time model = smf.ols('gross_income ~ branch_location', data=df_h).fit()\n",
    "                \n",
    "%time aov_table = sm.stats.anova_lm(model)\n",
    "print(aov_table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:12.454594Z",
     "start_time": "2021-07-29T22:23:12.444620Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['A - Yangon', 'C - Naypyitaw', 'B - Mandalay'], dtype=object)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_h.branch_location.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-29T22:23:12.472555Z",
     "start_time": "2021-07-29T22:23:12.456595Z"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wall time: 6 ms\n",
      "F-Statistic: 0.4423\n",
      "p-value: 0.2066\n"
     ]
    }
   ],
   "source": [
    "%time res = stats.f_oneway(df_h[df_h.branch_location == 'A - Yangon'].gross_income, df_h[df_h.branch_location == 'B - Mandalay'].gross_income,df_h[df_h.branch_location == 'C - Naypyitaw'].gross_income)\n",
    "print(f'F-Statistic: {res.statistic / 2:.4f}')\n",
    "print(f'p-value: {res.pvalue / 2:.4f}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-23T14:46:45.854018Z",
     "start_time": "2021-07-23T14:46:45.850208Z"
    }
   },
   "source": [
    "## Conclusion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Karena p-value is > α = 0.05, maka H0 tidak dapat ditolak / di reject sehingga:\n",
    "- Tidak ada perbedaan yang signifikan antara means dari gross income dari tiap toko."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-30T00:13:10.210862Z",
     "start_time": "2021-07-30T00:13:10.170856Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>column</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.650980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.439263</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.462770</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.150594</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.138442</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2995</th>\n",
       "      <td>0.933019</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2996</th>\n",
       "      <td>0.993083</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2997</th>\n",
       "      <td>0.119966</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2998</th>\n",
       "      <td>0.329720</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2999</th>\n",
       "      <td>0.010432</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>3000 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        column\n",
       "0     0.650980\n",
       "1     0.439263\n",
       "2     0.462770\n",
       "3     0.150594\n",
       "4     0.138442\n",
       "...        ...\n",
       "2995  0.933019\n",
       "2996  0.993083\n",
       "2997  0.119966\n",
       "2998  0.329720\n",
       "2999  0.010432\n",
       "\n",
       "[3000 rows x 1 columns]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-30T00:13:29.732018Z",
     "start_time": "2021-07-30T00:13:29.700016Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>branch</th>\n",
       "      <th>city</th>\n",
       "      <th>gross_income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>26.1415</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>3.8200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>16.2155</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>23.2880</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>30.2085</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>995</th>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>2.0175</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>B</td>\n",
       "      <td>Mandalay</td>\n",
       "      <td>48.6900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>1.5920</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>3.2910</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>30.9190</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    branch       city  gross_income\n",
       "0        A     Yangon       26.1415\n",
       "1        C  Naypyitaw        3.8200\n",
       "2        A     Yangon       16.2155\n",
       "3        A     Yangon       23.2880\n",
       "4        A     Yangon       30.2085\n",
       "..     ...        ...           ...\n",
       "995      C  Naypyitaw        2.0175\n",
       "996      B   Mandalay       48.6900\n",
       "997      A     Yangon        1.5920\n",
       "998      A     Yangon        3.2910\n",
       "999      A     Yangon       30.9190\n",
       "\n",
       "[1000 rows x 3 columns]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('supermarket_sales_p.csv')\n",
    "df_h = df[[\"branch\", \"city\", \"gross_income\"]]\n",
    "df_h"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2021-07-30T00:23:43.284258Z",
     "start_time": "2021-07-30T00:23:43.260261Z"
    }
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Branch</th>\n",
       "      <th>Location</th>\n",
       "      <th>Average of Gross Income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>Yangon</td>\n",
       "      <td>14.87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>Mandalay</td>\n",
       "      <td>15.23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>C</td>\n",
       "      <td>Naypyitaw</td>\n",
       "      <td>16.05</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Branch   Location  Average of Gross Income\n",
       "0      A     Yangon                    14.87\n",
       "1      B   Mandalay                    15.23\n",
       "2      C  Naypyitaw                    16.05"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_h.groupby([\"branch\", \"city\"]).mean().round(2).reset_index().rename(columns={'branch':'Branch','city':'Location', 'gross_income':'Average of Gross Income'})"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  },
  "nbTranslate": {
   "displayLangs": [
    "en"
   ],
   "hotkey": "alt-t",
   "langInMainMenu": true,
   "sourceLang": "en",
   "targetLang": "fr",
   "useGoogleTranslate": true
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": true,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
