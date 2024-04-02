# -*- coding: utf-8 -*-
{
   'name' : "Real_estate",
   'author': "Fatema Naiser",
   'category':'Real_Estate',
   'version':'17.0.0.2',
   'depends':['base','mail'],
   'data':[
         'security/security.xml',
         'security/ir.model.access.csv',
         'views/base_menu.xml',
         'views/property_view.xml',
         'views/owner_view.xml',
         'views/tag_view.xml',
         'views/building_view.xml',
         'views/interior.xml',
         'reports/property_report.xml',
       ],
   'assets' :{
       
       'web.assets_backend' : ['app_one\static\src\css\property.css'] 
              
              },
        
       
      
       
   'application':True,
   
}

