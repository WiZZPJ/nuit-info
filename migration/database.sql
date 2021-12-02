CREATE TABLE IF NOT EXISTS `User` (
    `idUser` INT(11) NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) NOT NULL,
    `passwordHash` VARCHAR(255) NOT NULL,
    `userEmail` VARCHAR(255) NOT NULL,
    `rank` INT(2) UNSIGNED NOT NULL DEFAULT '0',
    `token` VARCHAR(255) NOT NULL,
    `banned` BOOLEAN NOT NULL DEFAULT FALSE,
    "verified" BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (`idUser`), 
    UNIQUE (`username`), 
    UNIQUE (`userEmail`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Article` (
    `idArticle` INT(11) NOT NULL AUTO_INCREMENT,
    `slugArticle` VARCHAR(255) NOT NULL,
    `articleDate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `articleTitle` VARCHAR(255) NOT NULL,
    `articleContent` LONGTEXT NOT NULL,
    `articleAuthor` INT(11) NOT NULL,
    `accepted` BOOLEAN NOT NULL DEFAULT FALSE,
    `active` BOOLEAN NOT NULL,
    "articleAuthor" INT(11) NOT NULL,
    PRIMARY KEY (`idArticle`),
    UNIQUE (`slugArticle`)
) ENGINE = InnoDB;

ALTER TABLE `Article` 
    ADD CONSTRAINT `fk_Article_User`
        FOREIGN KEY (`articleAuthor`)  
        REFERENCES `User` (`idUser`);

CREATE TABLE IF NOT EXISTS `Media` (
    `idMedia` INT(11) NOT NULL AUTO_INCREMENT,
    `slugMedia` VARCHAR(255) NOT NULL,
    `pathMedia` VARCHAR(255) NOT NULL,
    `mimeType` VARCHAR(255) NOT NULL,
    `author` INT(11) NOT NULL,
    PRIMARY KEY (`idMedia`)
) ENGINE = InnoDB;

ALTER TABLE `Media`
    ADD CONSTRAINT `fk_Media_User`
        FOREIGN KEY (`author`)
        REFERENCES `User` (`idUser`);

CREATE TABLE IF NOT EXISTS `Category` (
    `idCategory` INT(11) NOT NULL AUTO_INCREMENT,
    `categoryName` VARCHAR(255) NOT NULL,
    `categoryDescription` VARCHAR(255) NOT NULL,
    "parentCategory" INT(11),
    PRIMARY KEY (`idCategory`)
) ENGINE = InnoDB;

ALTER TABLE "Category"
    ADD CONSTRAINT "fk_Category_Category"
        FOREIGN KEY ("parentCategory")
        REFERENCES "Category" ("idCategory");

CREATE TABLE IF NOT EXISTS `Boat` (
    `idBoat` INT(11) NOT NULL AUTO_INCREMENT,
    `nomBoat` VARCHAR(255) NOT NULL,
    `typeBoat` VARCHAR(255) NOT NULL,
    `detail` LONGTEXT NOT NULL,
    `beginningService` DATETIME NOT NULL,
    `endService` DATETIME,
    PRIMARY KEY (`idBoat`),
    UNIQUE (`nomBoat`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `Rescue` (
    `idRescue` INT(11) NOT NULL AUTO_INCREMENT,
    `rescueDate` DATETIME NOT NULL,
    `peopleSaved` INT(11) NOT NULL,
    `detail` TEXT NOT NULL,
    `source` JSON NOT NULL,
    `crew` JSON NOT NULL,
    `accepted` BOOLEAN DEFAULT FALSE,
    `active` BOOLEAN,
    "boatUsed" INT(11) NOT NULL,
    PRIMARY KEY (`idRescue`)
) ENGINE = InnoDB;

ALTER TABLE "Rescue"
    ADD CONSTRAINT "fk_Rescue_Boat"
        FOREIGN KEY ("boatUsed")
        REFERENCES "Boat" ("idBoat");

CREATE TABLE IF NOT EXISTS `Reward` (
    `idReward` INT(11) NOT NULL AUTO_INCREMENT,
    `entitled` VARCHAR(255) NOT NULL,
    "aRescue" INT(11) NOT NULL,
    PRIMARY KEY (`idReward`)
) ENGINE = InnoDB;

ALTER TABLE "Reward" 
    ADD CONSTRAINT "fk_Reward_Rescue"
        FOREIGN KEY ("aRescue")
        REFERENCES "Rescue" ("idRescue");

CREATE TABLE IF NOT EXISTS `Rescuer` (
    `firstName` VARCHAR(255) NOT NULL,
    `lastName` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`firstName`, `lastName`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS "RescueRescuer" (
    "aRescuer" INT(11) NOT NULL,
    "aRescue" INT(11) NOT NULL,
    PRIMARY KEY ("aRescuer", "aRescue")
) ENGINE = InnoDB;

ALTER TABLE "RescueRescuer"
    ADD CONSTRAINT "fk_RescueRescuer_Rescuer"
        FOREIGN KEY ("aRescuer")
        REFERENCES "Rescuer" ("idRescuer"),
    ADD CONSTRAINT "fk_RescueRescuer_Rescue"
        FOREIGN KEY ("aRescue")
        REFERENCES "Rescue" ("idRescue");

CREATE TABLE IF NOT EXISTS `ArticleMedia` (
    `aArticle` INT(11) NOT NULL,
    `aMedia` INT(11) NOT NULL,
    PRIMARY KEY (`aArticle`, `aMedia`)
) ENGINE = InnoDB;

ALTER TABLE `ArticleMedia`
    ADD CONSTRAINT `fk_ArticleMedia_Article`
        FOREIGN KEY (`aArticle`)
        REFERENCES `Article` (`idArticle`),
    ADD CONSTRAINT `fk_ArticleMedia_Media`
        FOREIGN KEY (`aMedia`)
        REFERENCES `Media` (`idMedia`);

CREATE TABLE IF NOT EXISTS "ArticleCategory" (
    "aArticle" INT(11) NOT NULL,
    "aCategory" INT(11) NOT NULL,
    PRIMARY KEY ("aArticle", "aCategory")
) ENGINE  = InnoDB;

ALTER TABLE "ArticleCategory" 
    ADD CONSTRAINT "fk_ArticleCategory_Article"
        FOREIGN KEY ("aArticle")
        REFERENCES "Article" ("idArticle"),
    ADD CONSTRAINT "fk_ArticleCategory_Category"
        FOREIGN KEY ("aCategory")
        REFERENCES "Category" ("idCategory");

CREATE TABLE IF NOT EXISTS "RescuerReward" (
    "aRescuer" INT(11) NOT NULL,
    "aReward" INT(11) NOT NULL,
    PRIMARY KEY ("aRescuer", "aReward");
) ENGINE = InnoDB;

ALTER TABLE "RescuerReward" 
    ADD CONSTRAINT "fk_RescuerReward_Rescuer"
        FOREIGN KEY ("aRescuer")
        REFERENCES "Rescuer" ("idRescuer"),
    ADD CONSTRAINT "fk_RescuerReward_Reward"
        FOREIGN KEY ("aReward")
        REFERENCES "Reward" ("idReward");