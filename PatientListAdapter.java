package com.example.a2021s_b07;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import com.example.a2021s_b07.Repository.Patient;

import java.util.List;

public class PatientListAdapter extends ArrayAdapter<Patient> {


    private Context mContext;
    private int mResource;

    public PatientListAdapter(Context context, int resource, List<Patient> objects) {
        super(context, resource, objects);
        this.mContext = context;
        this.mResource = resource;
    }

    /**
     * Holds variables in a View
     */
    private static class ViewHolder {
        TextView name;
        TextView birthday;
        TextView sex;
    }

    ViewHolder holder;

    @NonNull
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        //get the persons information
        String name = getItem(position).getName();
        String birthday = getItem(position).getBirthday();
        String sex = getItem(position).getSex();

        if(convertView == null){
            LayoutInflater inflater = LayoutInflater.from(mContext);
            convertView = inflater.inflate(mResource, parent, false);
            holder = new ViewHolder();
            holder.name = (TextView) convertView.findViewById(R.id.textView1);
            holder.birthday = (TextView) convertView.findViewById(R.id.textView2);
            holder.sex = (TextView) convertView.findViewById(R.id.textView3);

//            result = convertView;

            convertView.setTag(holder);
        }
        else{
            holder = (ViewHolder) convertView.getTag();
//            result = convertView;
        }

        holder.name.setText(name);
        holder.birthday.setText(birthday);
        holder.sex.setText(sex);

        return convertView;
    }
}
