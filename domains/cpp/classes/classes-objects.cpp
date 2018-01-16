#include <numeric>
class Student{
    private:
        vector<int> scores;
    public:
        void input(){
            for(int i = 1; i <= 5; i++){
                int temp;
                cin >> temp;
                scores.push_back(temp);
            }
        }
        int calculateTotalScore(){
            return accumulate(scores.begin(),scores.end(),0);
        }
};