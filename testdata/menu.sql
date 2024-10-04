create table `sys_menu` (
	`id` int (11),
	`name` varchar (150),
	`icon` varchar (300),
	`parent_id` int (11),
	`order_num` int (11),
	`path` varchar (600),
	`component` varchar (765),
	`menu_type` varchar (3),
	`perms` varchar (300),
	`create_time` date ,
	`update_time` date ,
	`remark` varchar (1500)
); 
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `component`, `menu_type`, `perms`, `create_time`, `update_time`, `remark`) values('1','系统管理','system','0','1','/sys','','M','','2024-07-04','2024-07-04','系统管理目錄');
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `component`, `menu_type`, `perms`, `create_time`, `update_time`, `remark`) values('2','營運管理','monitor','0','2','/bsns','','M','','2024-07-04','2024-07-04','業務管理目錄');
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `component`, `menu_type`, `perms`, `create_time`, `update_time`, `remark`) values('3','使用者管理','user','1','1','/sys/user','sys/user/index','C','system:user:list','2024-07-04','2024-10-01','使用者管理選單');
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `component`, `menu_type`, `perms`, `create_time`, `update_time`, `remark`) values('4','角色管理','logininfor','1','2','/sys/role','sys/role/index','C','system:role:list','2024-07-04','2024-07-04','角色管理選單');
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `component`, `menu_type`, `perms`, `create_time`, `update_time`, `remark`) values('5','選單管理','dict','1','3','/sys/menu','sys/menu/index','C','system:menu:list','2024-07-04','2024-07-04','選單管理選單');
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `component`, `menu_type`, `perms`, `create_time`, `update_time`, `remark`) values('6','部門管理','tree','2','1','/bsns/department','bsns/Department','C','','2024-07-04','2024-07-04','部門管理選單');
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `component`, `menu_type`, `perms`, `create_time`, `update_time`, `remark`) values('7','職位管理','post','2','2','/bsns/post','bsns/Post','C','','2024-07-04','2024-10-03','崗位管理選單');
