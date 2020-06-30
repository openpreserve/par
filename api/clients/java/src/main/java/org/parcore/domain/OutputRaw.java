package org.parcore.domain;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.util.Objects;

/**
 * PAR API
 * <p>
 * OutputRaw
 * <p>
 * Domain model for the OutputRaw object (part of the PreservationAction Core Entity)
 * <p>
 * OpenAPI spec version: 1.0.0
 * <p>
 * This class is based on code auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 */
@ApiModel(description = "A raw output from a preservation action")
@SuppressWarnings("unused")
public class OutputRaw {
    @SerializedName("description")
    private String description = null;

    @SerializedName("name")
    private String name = null;

    @SerializedName("value")
    private String value = null;

    /**
     * Get description
     *
     * @return description
     **/
    @ApiModelProperty(required = true, value = "")
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    /**
     * Get name
     *
     * @return name
     **/
    @ApiModelProperty(required = true, value = "")
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    /**
     * Get value
     *
     * @return value
     **/
    @ApiModelProperty(required = true, value = "")
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


    @Override
    public boolean equals(java.lang.Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        OutputRaw outputRaw = (OutputRaw) o;
        return Objects.equals(this.description, outputRaw.description) &&
                Objects.equals(this.name, outputRaw.name) &&
                Objects.equals(this.value, outputRaw.value);
    }

    @Override
    public int hashCode() {
        return Objects.hash(description, name, value);
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class OutputRaw {\n");

        sb.append("    description: ").append(toIndentedString(description)).append("\n");
        sb.append("    name: ").append(toIndentedString(name)).append("\n");
        sb.append("    value: ").append(toIndentedString(value)).append("\n");
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