-- auto-generated definition
create table REUS
(
    id                      int unsigned auto_increment
        primary key,
    state                   tinyint(1)                         comment 'Identification number of the state of the republic of the registered user',
    names                   varchar(50)                        comment 'Name (s) of the registered user',
    last_name               varchar(35)                        comment 'Paternal surname of the registered user',
    mother_last_name        varchar(35)                        comment 'Maternal surname of the registered user',
    rfc                     varchar(13)                        comment 'RFC of user',
    telephone_number        varchar(12)                        comment 'Fixed telephone number of the registered user',
    ext                     tinyint(2)                         comment 'Extension of the registered telephone number of the registered user',
    lada                    tinyint(2)                         comment 'Lada of the registered users landline',
    cell_phone_number       varchar(13)                       comment 'Mobile number of the registered user',
    lada                    tinyint(2)                         comment 'Lada of the registered mobile phone number of the registered user',
    private_mail            varchar(80)                        comment 'Private email of the registered user',
    office_mail             varchar(80)                        comment 'Registered user''s office email',
    high_date           timestamp default CURRENT_TIMESTAMP null comment 'Date when you registered in the portal of the
                                                                REUS the registered user',
    low_date       timestamp default CURRENT_TIMESTAMP        comment 'Date you unsubscribed from the portal of the
                                                                    REUS the registered user',
    effective_date timestamp default CURRENT_TIMESTAMP        comment 'Date on which the registration of the user in the REUS is concluded',
    status         tinyint(1)                                 comment 'User registration status 1 = current, 2 = movements, 3 = low'


)
    comment 'CONTAINS THE INFORMATION ABOUT PEOPLE IN THE LIST OF REUS' ENGINE=INNODB AUTO_INCREMENT=1 charset = utf8;