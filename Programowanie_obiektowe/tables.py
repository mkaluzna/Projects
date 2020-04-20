## Tworzenie tabeli do danych
import pandas as pd
from categories import Categories

class Tables():
    def __init__(self):
        self.kategorie = Categories()

        # Tabela wydatków
        zeros_exp = [0 for i in range(len(self.kategorie.exp_categories))]
        dict_exp = { 'Planowane': zeros_exp, 'Rzeczywiste': zeros_exp, 'Różnica': zeros_exp,
                     'St. realizacji budżetu (%)': zeros_exp}
        self.df_exp = pd.DataFrame(dict_exp, index = self.kategorie.exp_categories)

        # Tabela przychodów
        zeros_inc = [0 for j in range(len(self.kategorie.inc_categories))]
        dict_inc = {'Planowane': zeros_inc, 'Rzeczywiste': zeros_inc, 'Różnica': zeros_inc,
                    'St. realizacji budżetu (%)': zeros_inc}
        self.df_inc = pd.DataFrame(dict_inc, index = self.kategorie.inc_categories)

        # Dane szczegółowe wydatków
        zeros_details = [0 for k in range(31)]
        dict_details = {}
        for i in range(len(self.kategorie.exp_categories)):
            dict_details[self.kategorie.exp_categories[i]] = zeros_details
        self.df_details = pd.DataFrame(dict_details, index = [x for x in range(1,32)])

    def add_inc_cat(self, category):
        self.kategorie.add_inc_category(category)
        self.df_inc = self.df_inc.append({'Planowane': 0, 'Rzeczywiste': 0, 'Różnica': 0, 'St. realizacji budżetu (%)': 0},
                                         ignore_index=True)
        dict_names = {}
        for i in range(len(self.kategorie.inc_categories)):
            dict_names[i] = self.kategorie.inc_categories[i]
        self.df_inc.rename(index=dict_names, inplace=True)

    def add_exp_cat(self, category):
        self.kategorie.add_exp_category(category)
        self.df_exp = self.df_exp.append({'Planowane': 0, 'Rzeczywiste': 0, 'Różnica': 0, 'St. realizacji budżetu (%)': 0},
                                         ignore_index=True)
        dict_names1={}
        for i in range(len(self.kategorie.exp_categories)):
            dict_names1[i] = self.kategorie.exp_categories[i]
        self.df_exp.rename(index=dict_names1, inplace=True)

        self.df_details[category] = 0

    def show_df_exp(self):
        return self.df_exp

    def show_df_inc(self):
        return self.df_inc

    def show_df_details(self):
        return self.df_details

    def show_pieplot(self):
        df_pom = self.df_exp[['Planowane','Rzeczywiste']]
        df_pom.plot.pie(subplots = True, figsize=(10, 5), legend = True, autopct='%.2f', title = 'Wydatki')
        #plt.show(block=False)

    def show_barplot(self):
        sums_real = [self.df_inc.sum()[1], self.df_exp.sum()[1]]
        sums_plan = [self.df_inc.sum()[0], self.df_exp.sum()[0]]
        index = ['Przychody', 'Wydatki']
        df = pd.DataFrame({'Planowane': sums_plan, 'Rzeczywiste': sums_real}, index = index)
        df.plot.bar(rot=0, title = 'Porównanie wydatków i przychodów')
        #plt.show(block=False)

    def show_selected_days(self, a, b):
        return self.df_details[a-1:b]

if __name__ == "__main__":
    tabele = Tables()