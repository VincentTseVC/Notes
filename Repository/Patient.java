package com.example.a2021s_b07.Repository;

import java.io.Serializable;

public class Patient extends User implements Serializable {
    private String name;
    private String birthday;
    private String sex;

    public Patient(String name, String birthday, String sex) {
        this.birthday = birthday;
        this.name = name;
        this.sex = sex;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
}
