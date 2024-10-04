create table `sys_role` (
	`id` int (11),
	`name` varchar (90),
	`code` varchar (300),
	`create_time` date ,
	`update_time` date ,
	`remark` varchar (1500)
); 
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('1','超級管理員','admin','2024-07-04','2024-07-04','super user');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('2','普通角色','common','2024-07-04','2024-07-04','all business');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('3','內容管理者','content','2024-07-04','2024-07-04','for content ');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('4','系統使用者','sysuser','2024-07-04','2024-07-04','general user');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('5','開發者','dev','2024-07-04','2024-07-04','developer');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('6','業務管理','business','2024-07-04','2024-07-04','custom for bsns');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('20','硬體測試','hwtest','2024-07-04','2024-07-04','hw test');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('21','環境測試','envtest','2024-07-04','2024-07-04','environment test');
insert into `sys_role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`) values('56','CustomRole*','Custom','2024-10-03','2024-10-03','CustomRole for demo.');
