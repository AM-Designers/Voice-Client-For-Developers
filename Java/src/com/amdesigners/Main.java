package com.amdesigners;

import javax.swing.*;


class gui {
    public static void main(String args[]) {
        JFrame frame = new JFrame(Main.BasicConfiguration.app_name);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(Main.BasicConfiguration.width, Main.BasicConfiguration.height);

        // create a button that has image
        JButton button = new JButton(new ImageIcon(Main.BasicConfiguration.image));
        button.setSize(50, 50);

        button.setBounds(Main.BasicConfiguration.x, Main.BasicConfiguration.y, Main.BasicConfiguration.width, Main.BasicConfiguration.height);
        frame.add(button);
        frame.setVisible(true);
          

    }
}

public class Main {

    // =================== //
    // Basic Configuration //
    // =================== //
    public class BasicConfiguration {
        // Application Name
        public static String app_name = "Voice Assistant";
        public static String name = "John";
        public static String image =  System.getProperty("user.dir") + "\\src\\com\\amdesigners\\assets\\mic.png";
        
        public static int width = 400;
        public static int height = 600;
        
        public static int x = 0;
        public static int y = 0;
          
           
    }


    public static void main(String[] args) {
        System.out.println("Hello World!");
        // create a gui interface 
    }
}
