select st.name, sc.name from student st join school sc on sc.id = st.school_id 
group by sc.id;
-- bvb [name, name2, name3]