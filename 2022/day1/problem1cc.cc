#include <iostream>
#include <vector>
#include <set>

void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

bool isFormAlternativeSequence(int x, int y, const std::vector<int>& form) {
    int n = form.size();

    if (x > 1 || y > n || x >= y) {
        return false;
    }

    std::set<int> uniqueSet;
    for (int i = x - 1; i < y; ++i) {
        if (uniqueSet.find(form[i]) != uniqueSet.end()) {
            return false;
        }
        uniqueSet.insert(form[i]);
    }

    for (int i = x - 1; i < y - 2; ++i) {
        if ((form[i] > form[i + 1] && form[i + 1] < form[i + 2]) || (form[i] < form[i + 1] && form[i + 1] > form[i + 2])) {
            continue;
        } else {
            return false;
        }
    }

    return true;
}

int main() {
    std::vector<int> students = {5, 3, 8, 2, 6, 1, 7, 4};
    bubbleSort(students);

    std::vector<std::pair<int, int>> queries = {{2, 5}, {1, 4}, {3, 7}};

    for (const auto& query : queries) {
        bool result = isFormAlternativeSequence(query.first, query.second, students);
        if (result) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "no!" << std::endl;
        }
    }

    return 0;
}
