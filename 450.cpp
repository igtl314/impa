#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <sstream>

struct Employee {
    std::string prefix;
    std::string firstName;
    std::string lastName;
    std::string street;
    std::string homePhone;
    std::string workPhone;
    std::string box;
    std::string department;
};

int main(){
    int numDeparments;
    std::cin >> numDeparments;
    std::cin.ignore();
    std::vector<Employee> employees;

    for (int i = 0; i < numDeparments; ++i){
        std::string departmentName;
        getline(std::cin, departmentName);
        std::string input;
        while(getline(std::cin, input) && !input.empty() && input != ""){
            std::stringstream ss(input);
            Employee employee;

            getline(ss, employee.prefix, ',');
            getline(ss, employee.firstName, ',');
            getline(ss, employee.lastName, ',');
            getline(ss, employee.street, ',');
            getline(ss, employee.homePhone, ',');
            getline(ss, employee.workPhone, ',');
            getline(ss, employee.box, ',');
            employee.department = departmentName;

            employees.push_back(employee);
        }
    }
    std::sort(employees.begin(), employees.end(), [](const Employee& a, const Employee& b){
        return a.lastName < b.lastName;
    });

    for (const Employee employee : employees){
        std::cout << "----------------------------------------" << std::endl;
        std::cout << employee.prefix << " " << employee.firstName << " " << employee.lastName << std::endl;
        std::cout << employee.street << std::endl;
        std::cout << "Department: " << employee.department << std::endl;
        std::cout << "Home Phone: " << employee.homePhone << std::endl;
        std::cout << "Work Phone: " << employee.workPhone << std::endl;
        std::cout << "Campus Box: " << employee.box << std::endl;
    }
    return 0;
}