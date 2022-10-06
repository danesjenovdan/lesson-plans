<template>
  <ModalContainer @clicked-outside="$emit('clicked-outside')">
    <template #title>Download lesson</template>
    <template #default>
      <div class="instructions">{{ $t("download.instructions") }}</div>
      <div class="form-elements">
        <input v-model="nameLastName" type="text" placeholder="Name and last name" />
        <input v-model="organization" type="text" placeholder="Organization" />
        <input v-model="email" type="email" placeholder="your@email.example" />
        <input v-model="country" type="text" placeholder="Country" />
        <select v-model="role">
          <option disabled selected value>Role</option>
          <option value="teacher">teacher</option>
          <option value="coach">coach</option>
          <option value="parent">parent</option>
          <option value="student">student</option>
        </select>
      </div>
      <div class="buttons">
        <button class="download" @click="downloadFile">
          Download
          <img src="../assets/download.svg" />
        </button>
      </div>
    </template>
  </ModalContainer>
</template>

<script>
import ModalContainer from "./ModalContainer.vue";

export default {
  components: {
    ModalContainer,
  },
  props: {
    lesson: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      nameLastName: "",
      organization: "",
      email: "",
      country: "",
      role: "",
    };
  },
  mounted() {
    if (localStorage.nameLastName) {
      this.nameLastName = localStorage.nameLastName;
    }
    if (localStorage.organization) {
      this.organization = localStorage.organization;
    }
    if (localStorage.email) {
      this.email = localStorage.email;
    }
    if (localStorage.country) {
      this.country = localStorage.country;
    }
    if (localStorage.role) {
      this.role = localStorage.role;
    }
  },
  watch: {
    nameLastName(newNameLastName) {
      localStorage.nameLastName = newNameLastName;
    },
    organization(newOrganization) {
      localStorage.organization = newOrganization;
    },
    email(newEmail) {
      localStorage.email = newEmail;
    },
    country(newCountry) {
      localStorage.country = newCountry;
    },
    role(newRole) {
      localStorage.role = newRole;
    },
  },
  methods: {
    async downloadFile() {
      const downloadData = {
        name_lastname: this.nameLastName,
        organization: this.organization,
        email: this.email,
        country: this.country,
        role: this.role,
      };
      // const api = "http://localhost:8000/api/v1";
      const api = 'https://lesson-plans-backend.lb.djnd.si/api/v1';
      const result = await fetch(`${api}/download/`, {
        method: "post",
        headers: {
          "content-type": "application/json",
        },
        body: JSON.stringify(downloadData),
      });
      if (result.status === 201) {
        window.open(this.lesson.pdf);
      } else {
        alert(this.$t("download.error"));
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.instructions {
  margin-block: 24px;
  color: #252525;
  font-family: "Inter", sans-serif;
  font-size: 21px;
  line-height: 31px;
}

.form-elements {
  display: flex;
  flex-direction: column;
  gap: 12px;

  input,
  select {
    width: 100%;
    height: 50px;
    line-height: 50px;
    margin: 0;
    padding: 0 20px;
    border: 2px solid #000;
    font-family: "Inter", sans-serif;
    font-weight: 600;
    font-size: 18px;

    &:focus {
      background-color: #aefcd8;
      outline: none;
    }
  }
}

.buttons {
  margin-top: 30px;
  margin-bottom: 20px;

  button.download {
    position: relative;
    display: flex;
    align-items: center;
    gap: 23px;
    margin-inline: auto;
    padding: 16px 34px;
    background: #fff;
    border: 2px solid #000;
    font-family: "Inter", sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #252525;
    cursor: pointer;
    transform-style: preserve-3d;

    &::before {
      content: "";
      display: block;
      position: absolute;
      inset: 0;
      border: 2px solid #000;
      background-color: #aefcd8;
      transform: translate(9px, 9px) translateZ(-1px);
    }

    img {
      width: 20px;
      height: 25px;
    }
  }
}
</style>
