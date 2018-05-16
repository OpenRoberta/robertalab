package de.fhg.iais.roberta.persistence.bo;

import java.sql.Timestamp;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

import de.fhg.iais.roberta.util.Encryption;
import de.fhg.iais.roberta.util.Util1;

@Entity
@Table(name = "USER")
public class User implements WithSurrogateId {
    @Id
    @Column(name = "ID")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "ACCOUNT")
    private String account;

    @Column(name = "USER_NAME")
    private String userName;

    @Column(name = "PASSWORD")
    private String password;

    @Column(name = "EMAIL")
    private String email;

    @Enumerated(EnumType.STRING)
    @Column(name = "ROLE")
    private Role role;

    @Column(name = "CREATED")
    private Timestamp created;

    @Column(name = "LAST_LOGIN")
    private Timestamp lastLogin;

    @Column(name = "TAGS")
    private String tags;

    @Column(name = "ACTIVATED")
    private boolean activated;

    @Column(name = "YOUNGER_THAN_14")
    private boolean youngerThen14;

    protected User() {
        // Hibernate
    }

    /**
     * create a new program
     *
     * @param account the system wide unique account of a new user
     */
    public User(String account) {
        this.account = account;
        this.created = Util1.getNow();
        this.lastLogin = Util1.getNow();
    }

    public boolean isPasswordCorrect(String passwordToCheck) throws Exception {
        return Encryption.isPasswordCorrect(this.password, passwordToCheck);
    }

    public void setPassword(String password) throws Exception {
        this.password = Encryption.createHash(password);
    }

    /**
     * @return the userName
     */
    public String getUserName() {
        return this.userName;
    }

    /**
     * @param userName the userName to set
     */
    public void setUserName(String userName) {
        this.userName = userName;
    }

    /**
     * @return Email of User.
     */
    public String getEmail() {
        return this.email;
    }

    /**
     * Sets the New email
     *
     * @param email to be set
     */
    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * @return Role of the User (eg. Student, Teacher,etc.)
     */
    public Role getRole() {
        return this.role;
    }

    /**
     * Set role of the User.
     * 
     * @param role to be set.
     */
    public void setRole(Role role) {
        this.role = role;
    }

    public String getTags() {
        return this.tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }

    @Override
    public int getId() {
        return this.id;
    }

    public String getAccount() {
        return this.account;
    }

    public Timestamp getCreated() {
        return this.created;
    }

    /**
     * @return the Last login time.
     */
    public Timestamp getLastLogin() {
        return this.lastLogin;
    }

    /**
     * Sets the Last login time
     */
    public void setLastLogin() {
        this.lastLogin = Util1.getNow();
    }

    /**
     * @return true if Account is Activated.
     */
    public boolean isActivated() {
        return this.activated;
    }

    /**
     * @param activated True if Account is set to be Activated, else False.
     */
    public void setActivated(boolean activated) {
        this.activated = activated;
    }

    /**
     * @return true if Age is less than 14 years old.
     */
    public boolean isYoungerThen14() {
        return this.youngerThen14;
    }

    /**
     * Sets age Younger then 14 if True.
     * 
     * @param youngerThen14 is age less than 14 years?
     */
    public void setYoungerThen14(boolean youngerThen14) {
        this.youngerThen14 = youngerThen14;
    }

    /**
     * @return String containing Id, Account, and UserName.
     */
    @Override
    public String toString() {
        return "User [id=" + this.id + ", account=" + this.account + ", userName=" + this.userName + "]";
    }

}
