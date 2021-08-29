#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// std::string bloodgrp[8] = {"A+", "A-", "AB+", "AB-", "B+", "B-", "O+", "O-"};
// std::string hospitals[2] = {"h1", "h2"};

class admin{
    friend class bloodbank;
    private:
        std::string Name;
        std::string Password;
    public:
        admin(std::string name, std::string password)
        {
            Name = name;
            Password = password;
        }
};

class user{
    private:
    std::string Name;
    int blood_group;
    std::string Password;
    int Hospital;
    public:
    user(std::string name, std::string password, std::string hospital)
    {
        Name = name;
        Password = password;
        if(hospital=="h1") Hospital = 0;
        if(hospital=="h2") Hospital = 1;
    }
    int get_hospital()
    {
        return Hospital;
    }
    void set_hospital(string hospital_name)
    {
        if(hospital_name=="h1") Hospital = 0;
        if(hospital_name=="h2") Hospital = 1;
    }
    void set_bloodgrp(std::string blood)
    {  
        if(blood == "A+") blood_group = 0;
        if(blood == "A-") blood_group = 1;
        if(blood == "AB+") blood_group = 2;
        if(blood == "AB-") blood_group = 3;
        if(blood == "B+") blood_group = 4;
        if(blood == "B-") blood_group = 5;
        if(blood == "O+") blood_group = 6;
        if(blood == "O-") blood_group =7;
    }
    int get_bloodgrp()
    {
        return blood_group;
    }
};

class bloodbank{
    friend class admin;
    friend class user;
    public:
    int available_table[2][8] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1};

    int availability(int hospital_name,int blood_type)
    {
        if(available_table[hospital_name][blood_type]>0) return 1;
        else return 0;
        
    }
    void update_availtable(int hospital_name, int blood_type)
    {
        available_table[hospital_name][blood_type]++;
        cout<<"\n\n";
        cout<<"Thank you for donting!! Here is the updated data sheet"<<endl;
        cout<<"\n\n";
        printhospitalList();
    }
    void printhospitalList()
    {
        cout<<"   A+  A-  AB+ AB- B+  B-  O+  O-"<<endl;
        for(int i=0; i<2; i++)
        {
            if(i==0) cout<<"h1 ";
            if(i==1) cout<<"h2 ";
            for(int j=0; j<8; j++) cout<<available_table[i][j]<<"   ";
            cout<<"\n";
        }
        cout<<"\n\n\n";
    }
};

int main()
{
    bloodbank blood_database;
    //admin admin_1;
    //user user_1;
    int t=0;
    while(t==0)
    {
        cout<<"Enter 1 if admin and 2 if user"<<endl;
        int user_type;
        cin>>user_type;
        switch(user_type)
        {
            case 1:
            {
                cout<<"Hello admin!\n"<<"Please type in your username and password"<<endl;
                std::string name_temp;
                cin>>name_temp;
                std::string admin_1_pas;
                cin>>admin_1_pas;
                if(admin_1_pas == "key" && name_temp == "Boss") admin admin_1 = admin("Boss", "key");
                else {cout<<"Invalid password for admin"<<endl; cout<<"\n\n\n"; break;}
                cout<<"Welcome Boss to the bloodbank"<<endl;
                cout<<"Enter 1 to retrieve hospital list and availability status"<<endl;
                int task_manager;
                cin>>task_manager;
                if(task_manager==1) blood_database.printhospitalList();
                break;
            }
            case 2:
            {
                cout<<"Hello user!\n"<<"Please register to avail benefits of blood bank"<<endl;
                cout<<"Please give your name"<<endl;
                std::string name_temp;
                cin>>name_temp;
                cout<<"Enter your password"<<endl;
                std::string pas_temp;
                cin>>pas_temp;
                cout<<"Enter either h1 or h2 as your hospital"<<endl;
                std::string hos_temp;
                cin>>hos_temp;
                user user_1 = user(name_temp, pas_temp, hos_temp);
                cout<<"Enter 1 to request blood and 2 to donate blood"<<endl;
                int task_manager;
                cin>>task_manager;
                if(task_manager == 1)
                {
                    cout<<"Please enter your blood group"<<endl;
                    std::string blood;
                    cin>>blood;
                    user_1.set_bloodgrp(blood);
                    int blood_temp = user_1.get_bloodgrp();
                    int hos_temp = user_1.get_hospital();
                    int result = blood_database.availability(hos_temp, blood_temp);
                    if(result==1) 
                    {
                        cout<<"Your request has been accepted, please collect the sample"<<"\n\n\n"<<endl;

                    }
                    else
                    {
                        cout<<"Your request made is unavailable, sorry for the inconvinence"<<"\n\n\n"<<endl;
                    }      
                }
                else
                {   
                    cout<<"Please enter your blood group"<<endl;
                    std::string blood;
                    cin>>blood;
                    user_1.set_bloodgrp(blood);
                    int blood_temp = user_1.get_bloodgrp();
                    int hos_temp = user_1.get_hospital();
                    blood_database.update_availtable(hos_temp,blood_temp);
                }
            }
        }
    }
return 0;
}