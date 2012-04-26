DROP TABLE IF EXISTS `argo_user`;
CREATE TABLE IF NOT EXISTS `argo_user` (
    `uid` int(11) unsigned NOT NULL auto_increment,
    `userid` varchar(20) NOT NULL,
    `passwd` varchar(20),
    `nickname` varchar(20),
    `email` varchar(80),
    `userlevel` int(11) unsigned NOT NULL default 0,
    `netid`  varchar(20),
    `iconidx` varchar(20),

    `firstlogin` datetime NOT NULL default '0000-00-00 00:00:00',
    `firsthost` varchar(20),
    `lastlogin` datetime NOT NULL default '0000-00-00 00:00:00',
    `lasthost` varchar(20),
    `lastlogout` datetime NOT NULL default '0000-00-00 00:00:00',
    `numlogins` int(11) unsigned default 1,
    `numposts` int(11) unsigned default 0,
    `credit` int(11) unsigned default 0,
    `lastpost` datetime NOT NULL default '0000-00-00 00:00:00',
    `stay` int(11) unsigned default 0,
    `life`  int(11) default 365,
    `lastupdate` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,

    `birthday` date NOT NULL default '1990-01-28',
    `address` varchar(50), 
    `usertitle` varchar(20) NOT NULL default 'user',
    `gender`  int(11) unsigned default 1,
    `realname` varchar(20),
    
    PRIMARY KEY (`uid`),
    KEY `userid` (`userid`)

) ENGINE=InnoDB  DEFAULT CHARSET=GB2312;

