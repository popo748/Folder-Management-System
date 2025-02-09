<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">{{ title }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field v-model="folderData.title" label="Title" required />
                
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="$emit('close')">Close</v-btn>
          <v-btn color="blue darken-1" text @click="$emit('save', folderData)"
            >Save</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </template>
  
  <script>
  export default {
    props: {
      modelValue: {
        type: Boolean,
        required: true,
      },
      title: {
        type: String,
        required: true,
      },
      folder: {
        type: Object,
        required: true,
      },
    },
    emits: ["update:modelValue", "save", "close"],
    setup(props, { emit }) {
      const dialog = ref(props.modelValue);
      const folderData = ref({ ...props.folder });
  
      watch(dialog, (newValue) => {
        emit("update:modelValue", newValue);
      });
  
      watch(
        () => props.folder,
        (newFolder) => {
          folderData.value = { ...newFolder };
        }
      );
  
      onMounted(() => {
        folderData.value = { ...props.folder };
      });
  
      const updateFolderData = (field, value) => {
        folderData.value = { ...folderData.value, [field]: value };
      };
  
      return { dialog, folderData, updateFolderData };
    },
  };
  </script>