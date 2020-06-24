# file holds data for players and stats

import pandas as pd
from PyQt5.QtCore import QAbstractTableModel, Qt


class Database:
    def __init__(self, choice):
        qbCol = ["First Name", "Last Name", "Team", "GP", "Points", "Comp", "Pass Attempts", "Pass Yards", "Pass TDs",
                 "Rush Yards", "Rush TDs"]

        rbCol = ["First Name", "Last Name", "Team", "GP", "Points", "Rush Attempts", "Rush Yards", "Rush TDs",
                 "Targets", "Rec Yards", "Rec TDs"]

        recCol = ["First Name", "Last Name", "Team", "GP", "Points", "Targets", "Receptions", "Rec Yards", "Rec TDs"]

        kickerCol = ["First Name", "Last Name", "Team", "GP", "Points", "FG Made", "FG Att", "FG %", "XP Made"]

        defCol = ["First Name", "Last Name", "Team", "Points", "Sacks", "INTs", "Fumbles Rec", "Safeties", "Def TDs",
                  "Pts Against"]

        df_qb = pd.read_csv('Data/QB.csv', header=None, names=qbCol)
        df_rb = pd.read_csv('Data/RB.csv', header=None, names=rbCol)
        df_wr = pd.read_csv('Data/WR.csv', header=None, names=recCol)
        df_te = pd.read_csv('Data/TE.csv', header=None, names=recCol)
        df_k = pd.read_csv('Data/K.csv', header=None, names=kickerCol)
        df_def = pd.read_csv('Data/DEF.csv', header=None, names=defCol)

        data = {'QB': df_qb,
                'RB': df_rb,
                'WR': df_wr,
                'TE': df_te,
                'K': df_k,
                'DEF': df_def}

        if choice == 'Create':
            self.df_full = pd.concat(data)
        elif choice == 'Load':
            self.df_full = pd.read_csv('Saved/df.csv', index_col=[0, 1])

        self.players = self.df_full.loc[:, ['First Name', 'Last Name', 'Team']]

    def selectedPlayer(self, fname, lname):
        sp = self.df_full.loc[(self.df_full['First Name'] == fname) & (self.df_full['Last Name'] == lname)]
        index = sp.index[0]

        # Use to future reference, to know column names
        # name = (sp.iloc[0, 0] + ' ' + sp.iloc[0, 1])
        # team = sp.iloc[0, 2]
        # gp = sp.iloc[0, 3]
        # pts = sp.iloc[0, 4]
        # comp = sp.iloc[0, 5]
        # pAtt = sp.iloc[0, 6]
        # pYrd = sp.iloc[0, 7]
        # pTDs = sp.iloc[0, 8]
        # rYrd = sp.iloc[0, 9]
        # rTDs = sp.iloc[0, 10]
        # rAtt = sp.iloc[0, 11]
        # targets = sp.iloc[0, 12]
        # recY = sp.iloc[0, 13]
        # recTDs = sp.iloc[0, 14]
        # rec = sp.iloc[0, 15]
        # fgMade = sp.iloc[0, 16]
        # fgAtt = sp.iloc[0, 17]
        # fgPer = sp.iloc[0, 18]
        # xp = sp.iloc[0, 19]
        # sacks = sp.iloc[0, 20]
        # inter = sp.iloc[0, 21]
        # fumbles = sp.iloc[0, 22]
        # safeties = sp.iloc[0, 23]
        # dTDs = sp.iloc[0, 24]
        # ptsAgst = sp.iloc[0, 25]

        if index[0] == 'QB':
            stats = {
                'Pos': index[0],
                'PosNum': index[1],
                'Name': (sp.iloc[0, 0] + ' ' + sp.iloc[0, 1]),
                'Team': sp.iloc[0, 2],
                'Games Played': sp.iloc[0, 3],
                '2019 Fantasy Points': sp.iloc[0, 4],
                'Completions': sp.iloc[0, 5],
                'Pass Attempts': sp.iloc[0, 6],
                'Pass Yards': sp.iloc[0, 7],
                'Pass TDs': sp.iloc[0, 8],
                'Rush Yards': sp.iloc[0, 9],
                'Rush TDs': sp.iloc[0, 10]
            }
            qbPlayer = self.int2str(**stats)
            return qbPlayer

        elif index[0] == 'RB':
            stats = {
                'Pos': index[0],
                'PosNum': index[1],
                'Name': (sp.iloc[0, 0] + ' ' + sp.iloc[0, 1]),
                'Team': sp.iloc[0, 2],
                'Games Played': sp.iloc[0, 3],
                '2019 Fantasy Points': sp.iloc[0, 4],
                'Rush Attempts': sp.iloc[0, 11],
                'Rush Yards': sp.iloc[0, 9],
                'Rush TDs': sp.iloc[0, 10],
                'Targets': sp.iloc[0, 12],
                'Receiving Yards': sp.iloc[0, 13],
                'Receiving TDs': sp.iloc[0, 14]
            }
            rbPlayer = self.int2str(**stats)
            return rbPlayer

        elif index[0] == 'WR' or index[0] == 'TE':
            stats = {
                'Pos': index[0],
                'PosNum': index[1],
                'Name': (sp.iloc[0, 0] + ' ' + sp.iloc[0, 1]),
                'Team': sp.iloc[0, 2],
                'Games Played': sp.iloc[0, 3],
                '2019 Fantasy Points': sp.iloc[0, 4],
                'Targets': sp.iloc[0, 12],
                'Receptions': sp.iloc[0, 15],
                'Receiving Yards': sp.iloc[0, 13],
                'Receiving TDs': sp.iloc[0, 14]
            }
            wrPlayer = self.int2str(**stats)
            return wrPlayer

        elif index[0] == 'K':
            stats = {
                'Pos': index[0],
                'PosNum': index[1],
                'Name': (sp.iloc[0, 0] + ' ' + sp.iloc[0, 1]),
                'Team': sp.iloc[0, 2],
                'Games Played': sp.iloc[0, 3],
                '2019 Fantasy Points': sp.iloc[0, 4],
                'Field Goals Made': sp.iloc[0, 16],
                'Field Goal Attempt': sp.iloc[0, 17],
                'Field Goal %': sp.iloc[0, 18],
                'Extra Points Made': sp.iloc[0, 19]
            }
            kPlayer = self.int2str(**stats)
            return kPlayer
        else:
            stats = {
                'Pos': index[0],
                'PosNum': index[1],
                'Name': (sp.iloc[0, 0] + ' ' + sp.iloc[0, 1]),
                'Team': sp.iloc[0, 2],
                '2019 Fantasy Points': sp.iloc[0, 4],
                'Sacks': sp.iloc[0, 20],
                'Interceptions': sp.iloc[0, 21],
                'Fumbles Recovered': sp.iloc[0, 22],
                'Safeties': sp.iloc[0, 23],
                'Points Against': sp.iloc[0, 25],
                'Defensive TDs': sp.iloc[0, 24]
            }
            defense = self.int2str(**stats)
            return defense

    def int2str(self, **stat):
        strConv = stat.items()
        playerStat = {str(key): str(value) for key, value in strConv}
        return playerStat

    # TODO create if statement for fname and fname having entries
    def playerSea(self, pos, fName, lName):
        if pos == 'All':
            if len(fName) == 0 and len(lName) == 0:
                model = PandasModel(self.players)
                return model
            if len(fName) > 0 and len(lName) == 0:
                fnPlayers = self.players.loc[self.players['First Name'].str.contains(fName)]
                model = PandasModel(fnPlayers)
                return model
            if len(fName) == 0 and len(lName) > 0:
                lnPlayers = self.players.loc[self.players['Last Name'].str.contains(lName)]
                model = PandasModel(lnPlayers)
                return model
        elif pos == 'DEF':
            defense = (self.df_full.loc[['DEF'], ['First Name', 'Last Name', 'Team']])
            model = PandasModel(defense)
            return model
        else:
            posSearch = self.players.loc[pos]
            if len(fName) == 0 and len(lName) == 0:
                model = PandasModel(posSearch)
                return model
            if len(fName) > 0 and len(lName) == 0:
                fnPlayers = posSearch.loc[posSearch['First Name'].str.contains(fName)]
                model = PandasModel(fnPlayers)
                return model
            if len(fName) == 0 and len(lName) > 0:
                lnPlayers = posSearch.loc[posSearch['Last Name'].str.contains(lName)]
                model = PandasModel(lnPlayers)
                return model
        return None

    def blank(self):
        blank = self.players.iloc[0:0]
        model = PandasModel(blank)
        return model

    def getTop(self, position):
        fiveList = [position]
        topFive = self.players.loc[f'{position}', ['First Name', 'Last Name']].head(5)
        for idx, row in topFive.iterrows():
            name = f"{row['First Name']} {row['Last Name']}"
            fiveList.append(name)

        return fiveList

    def removePlayer(self, *idx):
        self.df_full.drop(idx, inplace=True)
        self.players.drop(idx, inplace=True)

    # TODO use file finder to save to location
    def saveDF(self):
        self.df_full.to_csv('Saved/df.csv', na_rep='', float_format='%.1f', header=True, index=True)


# class creates model to be used on QTableView in MainWindow.py
class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
