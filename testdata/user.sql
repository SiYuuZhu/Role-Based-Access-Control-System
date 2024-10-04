create table `sys_user` (
	`id` int (11),
	`username` varchar (300),
	`password` varchar (300),
	`avatar` varchar (765),
	`email` varchar (300),
	`phonenumber` varchar (33),
	`login_date` date ,
	`status` int (11),
	`create_time` date ,
	`update_time` date ,
	`remark` varchar (1500)
); 
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('1','yuuu','e10adc3949ba59abbe56e057f20f883e','20240926234711.jpg','siyuuzhu@gmail.com','0905190890','2024-08-09','1','2024-08-08','2024-10-03','SUPERUSER');
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('3','user3','e10adc3949ba59abbe56e057f20f883e','avatar1.jpg','uni208018@gmail.com','11122233344','2024-09-09','1','2024-08-08','2024-10-03','TEST-ACC');
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('6','user6','e10adc3949ba59abbe56e057f20f883e','avatar2.jpg','user666@mail.com','06661666',NULL,'0',NULL,'2024-09-29',NULL);
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('11','testuser11','e10adc3949ba59abbe56e057f20f883e','avatar3.jpg','testuser11@mail.com','01110111',NULL,'1',NULL,'2024-09-29',NULL);
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('15','test-user15','e10adc3949ba59abbe56e057f20f883e','default.jpg','sizhu@gmail.com','12345678900',NULL,'0','2024-01-01','2024-09-30','禁用帳號2');
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('18','yuyu','e10adc3949ba59abbe56e057f20f883e','avatar3.jpg','yuyu@gmail.com','0905190190','2024-09-29','1','2024-09-29','2024-10-02','p');
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('20','tester','e10adc3949ba59abbe56e057f20f883e','default.jpg','tester@mail.com','0800123123',NULL,'1','2024-09-30','2024-10-03','');
insert into `sys_user` (`id`, `username`, `password`, `avatar`, `email`, `phonenumber`, `login_date`, `status`, `create_time`, `update_time`, `remark`) values('43','demoacc','fcea920f7412b5da7be0cf42b8c93759','20241003235111.jpg','demo@gmail.com','0900111444',NULL,'1','2024-10-03','2024-10-03','demo');
