package org.parcore.domain;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

/**
 * A file that is an input or output of a preservation action
 */
@SuppressWarnings("unused")
@ApiModel(description = "A file that is an input or output of a preservation action")
public class ParFile {

    @SerializedName("filepath")
    private String filepath = null;

    /**
     * Get filepath
     * @return filepath
     **/
    @ApiModelProperty(value = "")
    public String getFilepath() {
        return filepath;
    }

    public void setFilepath(String filepath) {
        this.filepath = filepath;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        ParFile parFile = (ParFile) o;
        return Objects.equals(this.filepath, parFile.filepath);
    }

    @Override
    public int hashCode() {
        return Objects.hash(filepath);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class ParFile {\n");

        sb.append("    filepath: ").append(toIndentedString(filepath)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(java.lang.Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
