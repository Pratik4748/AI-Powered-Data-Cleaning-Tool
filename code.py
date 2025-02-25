{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "243838be-a020-4610-b92c-1bd4aefb8a93",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a74e26c5-b43c-414b-a927-31cdd725052f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from mistralai import Mistral"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7524ad4c-2099-46ee-88fc-8839f3102a61",
   "metadata": {},
   "outputs": [],
   "source": [
    "api_key=os.getenv(\"MISTRAL_API_KEY\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "bf0ee911-9af3-4d40-a623-fff1a4901d5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "59e6eee7-852a-4f74-b9bc-65494571d01f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Customer Name               Email     Age Purchase Amount  \\\n",
      "0             John Doe  john.doe@email.com      25            $100   \n",
      "1           Jane Smith    jane_smith@email  thirty         200 USD   \n",
      "2                 NULL    robert@email.com      45   Three Hundred   \n",
      "3         Robert Brown                  NA      ??             400   \n",
      "4  Anne-Marie O'Conner      anne@email.com      27          500.00   \n",
      "\n",
      "  Date of Purchase  \n",
      "0       2024/01/05  \n",
      "1       2024-02-15  \n",
      "2     Feb 20, 2024  \n",
      "3       15-03-2024  \n",
      "4   March 10, 2024  \n"
     ]
    }
   ],
   "source": [
    "# Sample dataset\n",
    "data = {\n",
    "    \"Customer Name\": [\"John Doe\", \"Jane Smith\", \"NULL\", \"Robert Brown\", \"Anne-Marie O'Conner\"],\n",
    "    \"Email\": [\"john.doe@email.com\", \"jane_smith@email\", \"robert@email.com\", \"NA\", \"anne@email.com\"],\n",
    "    \"Age\": [\"25\", \"thirty\", \"45\", \"??\", \"27\"],\n",
    "    \"Purchase Amount\": [\"$100\", \"200 USD\", \"Three Hundred\", \"400\", \"500.00\"],\n",
    "    \"Date of Purchase\": [\"2024/01/05\", \"2024-02-15\", \"Feb 20, 2024\", \"15-03-2024\", \"March 10, 2024\"]\n",
    "}\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "97eabeb6-0f5a-447a-83f6-00f1f1b365b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df =pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1b7a3297-1685-4c7f-bd68-de0e5de484bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Customer Name               Email     Age Purchase Amount  \\\n",
      "0             John Doe  john.doe@email.com      25            $100   \n",
      "1           Jane Smith    jane_smith@email  thirty         200 USD   \n",
      "2                 NULL    robert@email.com      45   Three Hundred   \n",
      "3         Robert Brown                  NA      ??             400   \n",
      "4  Anne-Marie O'Conner      anne@email.com      27          500.00   \n",
      "\n",
      "  Date of Purchase  \n",
      "0       2024/01/05  \n",
      "1       2024-02-15  \n",
      "2     Feb 20, 2024  \n",
      "3       15-03-2024  \n",
      "4   March 10, 2024  \n"
     ]
    }
   ],
   "source": [
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54df2cdc-d372-4070-b853-94278f38abe7",
   "metadata": {},
   "source": [
    "The above data contains Missing values,inconsistencies,improper formating :\n",
    "<br> 1.Customer Name contains \"NULL\" Value.\n",
    "<br> 2.Email contains \"NA\" and incorrect email format.\n",
    "<br> 3.Age contains incorrect data type \"thirty\".\n",
    "<br> 4.Purchase Amount contains incorrect data type \"Three Hundred\" and incorrect currency format."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9513cb8b-9be7-42da-a968-ff92225cff5c",
   "metadata": {},
   "source": [
    "# Cleaning of data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fe2fb117-adec-422a-98a9-a5747b52086e",
   "metadata": {},
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
       "      <th>Customer Name</th>\n",
       "      <th>Email</th>\n",
       "      <th>Age</th>\n",
       "      <th>Purchase Amount</th>\n",
       "      <th>Date of Purchase</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>John Doe</td>\n",
       "      <td>john.doe@email.com</td>\n",
       "      <td>25</td>\n",
       "      <td>$100</td>\n",
       "      <td>2024/01/05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Jane Smith</td>\n",
       "      <td>jane_smith@email</td>\n",
       "      <td>thirty</td>\n",
       "      <td>200 USD</td>\n",
       "      <td>2024-02-15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>robert@email.com</td>\n",
       "      <td>45</td>\n",
       "      <td>Three Hundred</td>\n",
       "      <td>Feb 20, 2024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Robert Brown</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>400</td>\n",
       "      <td>15-03-2024</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Anne-Marie O'Conner</td>\n",
       "      <td>anne@email.com</td>\n",
       "      <td>27</td>\n",
       "      <td>500.00</td>\n",
       "      <td>March 10, 2024</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Customer Name               Email     Age Purchase Amount  \\\n",
       "0             John Doe  john.doe@email.com      25            $100   \n",
       "1           Jane Smith    jane_smith@email  thirty         200 USD   \n",
       "2                  NaN    robert@email.com      45   Three Hundred   \n",
       "3         Robert Brown                 NaN     NaN             400   \n",
       "4  Anne-Marie O'Conner      anne@email.com      27          500.00   \n",
       "\n",
       "  Date of Purchase  \n",
       "0       2024/01/05  \n",
       "1       2024-02-15  \n",
       "2     Feb 20, 2024  \n",
       "3       15-03-2024  \n",
       "4   March 10, 2024  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Replacing missing values with \"NAN\"\n",
    "df.replace(to_replace = [\"NULL\",\"NA\",\"??\"],value=np.nan,inplace = True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e96f87a1-ef27-456e-b844-e02f75719c46",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Handling missing values and \"NAN\" values in Email column\n",
    "def clean_email(email):\n",
    "    if pd.isna(email) or \"@\" not in email: # return nan if email is null or \"@\" is absent in email\n",
    "        return np.nan\n",
    "\n",
    "    email = email.strip().lower() # removes extra spaces and gives email in lower case\n",
    "    email = re.sub(r\"\\s+\",\"\",email) # removes all spaces inside the email\n",
    "\n",
    "    if not email.endswith(\".com\"):\n",
    "        email = re.sub(r\"\\.[a-z]+$\",\".com\",email)\n",
    "        if not email.endswith(\".com\"):\n",
    "            email+=\".com\" # Append \".com\" is still missing    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b0d6f723-f661-492a-abb7-3ffec2921a72",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert string age into numeric age column\n",
    "def convert_age(age):\n",
    "    age_map = {\"thirty\":30}\n",
    "    if isinstance(age,str):\n",
    "       return age_map.get(age.lower(),age)\n",
    "    else :\n",
    "        return age\n",
    "df[\"Age\"] = df[\"Age\"].astype(str).apply(convert_age)\n",
    "df[\"Age\"] = pd.to_numeric(df[\"Age\"],errors=\"coerce\") # convert age into numeric"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b3b3fb3b-268b-4ba4-9bd3-1115ed86c6fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Remove non-numeric values from purchase amount\n",
    "def clean_currency(amount):\n",
    "    if pd.isna(amount) :\n",
    "        return np.nan\n",
    "    amount = re.sub(r\"[^\\d.]\",\"\",amount) # removes non numeric characters\n",
    "    amount_map = {\"Three Hundred\":30}\n",
    "    if isinstance(amount,str):\n",
    "        return amount_map.get(amount.lower(),amount)\n",
    "    else :\n",
    "        return amount\n",
    "df[\"Purchase Amount\"] = df[\"Purchase Amount\"].astype(str).apply(clean_currency)\n",
    "df[\"Purchase Amount\"] = pd.to_numeric(df[\"Purchase Amount\"],errors = \"coerce\")           "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "04de77b7-5cbd-49f5-92e6-89851b9f6794",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[\"Date of Purchase\"]=pd.to_datetime(df[\"Date of Purchase\"],errors=\"coerce\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "813dea2a-b18e-4ae3-939b-c3f1016e71f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ai_clean_column(column_name,column_values):\n",
    "    prompt = f\"\"\"\n",
    "    The Following column \"{column_name}\" contains messy data. Please clean and standardize it.\n",
    "    Original Values : {column_values}\n",
    "    \n",
    "    Cleaned Values :\n",
    "    \"\"\"\n",
    "    client = Mistral(api_key=api_key)\n",
    "\n",
    "    chat_response = client.chat.complete(\n",
    "        model= \"mistral-large-latest\",\n",
    "        messages = [{\"role\": \"user\",\"content\": prompt }])\n",
    "    print(chat_response.choices[0].message.content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c2eda492-de9f-4205-b8ff-69cea71a0258",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "To clean and standardize the \"Age\" column, we need to handle the `nan` value and ensure that all values are in a consistent format. Here's how we can proceed:\n",
      "\n",
      "1. Convert the string representations of numbers to actual numbers.\n",
      "2. Handle the `nan` value by either removing it or replacing it with a sensible value (e.g., the mean of the other ages).\n",
      "\n",
      "Let's assume we want to replace the `nan` value with the mean of the other ages.\n",
      "\n",
      "Original Values: `['25.0', '30.0', '45.0', 'nan', '27.0']`\n",
      "\n",
      "Steps to clean and standardize:\n",
      "\n",
      "1. Convert the string representations to float.\n",
      "2. Calculate the mean of the valid ages.\n",
      "3. Replace `nan` with the mean.\n",
      "4. Convert all values to integers (assuming ages should be integers).\n",
      "\n",
      "Here's the Python code to achieve this:\n",
      "\n",
      "```python\n",
      "import numpy as np\n",
      "\n",
      "# Original values\n",
      "original_values = ['25.0', '30.0', '45.0', 'nan', '27.0']\n",
      "\n",
      "# Convert to float, handling 'nan'\n",
      "age_values = [float(value) if value != 'nan' else np.nan for value in original_values]\n",
      "\n",
      "# Calculate the mean of the valid ages\n",
      "mean_age = np.nanmean(age_values)\n",
      "\n",
      "# Replace 'nan' with the mean age\n",
      "cleaned_values = [int(age) if not np.isnan(age) else int(mean_age) for age in age_values]\n",
      "\n",
      "print(cleaned_values)\n",
      "```\n",
      "\n",
      "The resulting `cleaned_values` will be:\n",
      "\n",
      "```python\n",
      "[25, 30, 45, 31, 27]\n",
      "```\n",
      "\n",
      "Explanation:\n",
      "- The mean age of the valid values (25, 30, 45, 27) is `(25 + 30 + 45 + 27) / 4 = 127 / 4 = 31.75`, which we round to 31.\n",
      "- The `nan` value is replaced with 31.\n",
      "- All values are converted to integers.\n",
      "\n",
      "So, the cleaned and standardized values are:\n",
      "\n",
      "`[25, 30, 45, 31, 27]`\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "# Example: Fix missing Age values using AI\n",
    "cleaned_ages = ai_clean_column(\"Age\", df[\"Age\"].astype(str).tolist())\n",
    "print(cleaned_ages)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
