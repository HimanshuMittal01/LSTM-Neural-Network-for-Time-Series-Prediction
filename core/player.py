class Player:
    def __init__(self, name, money, bet_chips, predictions, true_data):
        self.name = name
        self.money = money
        self.bet_chips = bet_chips
        self.predictions = predictions
        self.true_data = true_data
    def bet(self):
        original_count = 1
        # for i in range(len(self.predictions)):
        #     for j in range(1, len(self.predictions[i])-5):
        #         if self.predictions[i][j+5] - self.predictions[i][j-1]>0:
        #             if self.true_data[original_count][0] - self.true_data[original_count-1][0]>0:
        #                 self.money += self.bet_chips
        #             else:
        #                 self.money -= self.bet_chips
        #         else:
        #             if self.true_data[original_count][0] - self.true_data[original_count-1][0]<=0:
        #                 self.money += self.bet_chips
        #             else:
        #                 self.money -= self.bet_chips
        #         original_count += 1
        #     for j in range(5):
        #         if self.predictions[i][49] - self.predictions[i][49-5]>0:
        #             if self.true_data[original_count][0] - self.true_data[original_count-1][0]>0:
        #                 self.money += self.bet_chips
        #             else:
        #                 self.money -= self.bet_chips
        #         else:
        #             if self.true_data[original_count][0] - self.true_data[original_count-1][0]<=0:
        #                 self.money += self.bet_chips
        #             else:
        #                 self.money -= self.bet_chips
        #         original_count += 1
        #     original_count += 1

        for i in range(len(self.predictions)-1):
            if self.predictions[i]-self.true_data[i]>0:
                if self.true_data[i+1]-self.true_data[i]>0:
                    self.money += self.bet_chips
                else:
                    self.money -= self.bet_chips
            else:
                if self.true_data[i+1]-self.true_data[i]<=0:
                    self.money += self.bet_chips
                else:
                    self.money -= self.bet_chips
        

        print(self.money)