

SELECT * FROM MADB.DETECT_STATISTICS where OPERATION_ID= 589;

The hourly rate of persons for operation 589 per day

SELECT OBJECT, HOUR(DATE_TIME) as datePart,        
             avg(VALUE)               
             FROM DETECT_STATISTICS WHERE    
             OBJECT in('Persons') and OPERATION_ID IN (589)         
             GROUP BY OBJECT, datePart order by datePart;
             

       chart bar Hourly comparison of incoming and outgoing visitors for operation 592
       
      SELECT  hour(DATE_TIME) AS dayid,OBJECT,( MAX(VALUE) -   MIN(VALUE)  )AS 
      VALUE  FROM DETECT_STATISTICS       WHERE   
      OPERATION_ID = 592 AND (OBJECT = 'in' OR OBJECT = 'out') GROUP BY dayid,OBJECT ORDER BY dayid, OBJECT
      
queyy1 SELECT  DAYOFWEEK(DATE_TIME) AS dayid,OBJECT,( MAX(VALUE) -   MIN(VALUE)  )AS count FROM DETECT_STATISTICS  WHERE     OPERATION_ID = 592 AND (OBJECT = 'in' OR OBJECT = 'out') GROUP BY dayid,OBJECT ORDER BY dayid, OBJECT
             
       ----------------
    The hourly rate count   of incoming visitors  per day for operation 589 
       
       SELECT HOUR(DATE_TIME) as hourPart,         
       ( MAX(VALUE) -   MIN(VALUE)  )AS 
      VALUE                
       
       FROM DETECT_STATISTICS WHERE                  OBJECT in('in') and OPERATION_ID IN (592) 
       GROUP BY hourPart order by hourPart;
       --------------
       The hourly rate count   of outgoing  visitors  per day for operation 592 
          SELECT HOUR(DATE_TIME) as hourPart,         
       ( MAX(VALUE) -   MIN(VALUE)  )AS 
      VALUE                
       
       FROM DETECT_STATISTICS WHERE                  OBJECT in('out') and OPERATION_ID IN (592) 
       GROUP BY hourPart order by hourPart;
       --------------
       The hourly rate count   of outgoing  visitors  per day for operation 602  
       
       ------------
     Average time spent per cashier  with customer  hourly by the during the day for operation 602 
     
     SELECT OBJECT,  hour(DATE_TIME) as datePart,       
     avg(VALUE)                     FROM DETECT_STATISTICS 
     WHERE     OBJECT in('c1') and OPERATION_ID IN (602)       
     GROUP BY OBJECT, datePart order by datePart;
     
     SELECT HOUR(DATE_TIME) as hourPart,        
             avg(TOTAL_TIME)               
             FROM DETECT_STATISTICS WHERE    
             OBJECT in('dwel time') and OPERATION_ID IN (60)         
             GROUP BY hourPart order by hourPart;
             
             compare Average time spent each cashier with customer roughly by the during the day for operation 602
     
       
       
